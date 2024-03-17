import struct

from Crypto.Hash import CMAC
from Crypto.Cipher import AES

from cereal import car

SteerControlType = car.CarParams.SteerControlType

def secoc_add_cmac(key, trip_cnt, reset_cnt, msg_cnt, msg):
  # TODO: clean up conversion to and from hex

  addr, t, payload, bus = msg
  reset_flag = reset_cnt & 0b11
  msg_cnt_flag = msg_cnt & 0b11
  payload = payload[:4]

  # Step 1: Build Freshness Value (48 bits)
  # [Trip Counter (16 bit)][[Reset Counter (20 bit)][Message Counter (8 bit)][Reset Flag (2 bit)][Padding (2 bit)]
  freshness_value = struct.pack('>HI', trip_cnt, (reset_cnt << 12) | ((msg_cnt & 0xff) << 4) | (reset_flag << 2))

  # Step 2: Build data to authenticate (96 bits)
  # [Message ID (16 bits)][Payload (32 bits)][Freshness Value (48 bits)]
  to_auth = struct.pack('>H', addr) + payload + freshness_value

  # Step 3: Calculate CMAC (28 bit)
  cmac = CMAC.new(key, ciphermod=AES)
  cmac.update(to_auth)
  mac = cmac.digest().hex()[:7] # truncated MAC

  # Step 4: Build message
  # [Payload (32 bit)][Message Counter Flag (2 bit)][Reset Flag (2 bit)][Authenticator (28 bit)]
  msg_cnt_rst_flag = struct.pack('>B', (msg_cnt_flag << 2) | reset_flag).hex()[1]
  msg = payload.hex() + msg_cnt_rst_flag + mac
  payload = bytes.fromhex(msg)

  return (addr, t, payload, bus)

def build_sync_mac(key, trip_cnt, reset_cnt, id_=0xf):
    id_ = struct.pack('>H', id_) # 16
    trip_cnt = struct.pack('>H', trip_cnt) # 16
    reset_cnt = struct.pack('>I', reset_cnt << 12)[:-1] # 20 + 4 padding

    to_auth = id_ + trip_cnt + reset_cnt # SecOC 11.4.1.1 page 138

    cmac = CMAC.new(key, ciphermod=AES)
    cmac.update(to_auth)

    msg = "0" + cmac.digest().hex()[:7]
    msg = bytes.fromhex(msg)
    return struct.unpack('>I', msg)[0]

def create_steer_command(packer, steer, steer_req):
  """Creates a CAN message for the Toyota Steer Command."""

  values = {
    "STEER_REQUEST": steer_req,
    "STEER_TORQUE_CMD": steer,
    "SET_ME_1": 1,
  }
  return packer.make_can_msg("STEERING_LKA", 0, values)


def create_lta_steer_command(packer, steer_control_type, steer_angle, steer_req, frame, torque_wind_down):
  """Creates a CAN message for the Toyota LTA Steer Command."""

  values = {
    "COUNTER": frame + 128,
    "SETME_X1": 1,  # suspected LTA feature availability
    # 1 for TSS 2.5 cars, 3 for TSS 2.0. Send based on whether we're using LTA for lateral control
    "SETME_X3": 1 if steer_control_type == SteerControlType.angle else 3,
    "PERCENTAGE": 100,
    "TORQUE_WIND_DOWN": torque_wind_down,
    "ANGLE": 0,
    "STEER_ANGLE_CMD": steer_angle,
    "STEER_REQUEST": steer_req,
    "STEER_REQUEST_2": steer_req,
    "CLEAR_HOLD_STEERING_ALERT": 0,
  }
  return packer.make_can_msg("STEERING_LTA", 0, values)

def create_lta_steer_command_2(packer, frame):
  values = {
    "COUNTER": frame + 128,
  }
  return packer.make_can_msg("STEERING_LTA_2", 0, values)

def create_accel_command(packer, accel, pcm_cancel, standstill_req, lead, acc_type, fcw_alert, distance):
  # TODO: find the exact canceling bit that does not create a chime
  values = {
    "ACCEL_CMD": accel,
    "ACC_TYPE": acc_type,
    "DISTANCE": distance,
    "MINI_CAR": lead,
    "PERMIT_BRAKING": 1,
    "RELEASE_STANDSTILL": not standstill_req,
    "CANCEL_REQ": pcm_cancel,
    "ALLOW_LONG_PRESS": 1,
    "ACC_CUT_IN": fcw_alert,  # only shown when ACC enabled
  }
  return packer.make_can_msg("ACC_CONTROL", 0, values)


def create_acc_cancel_command(packer):
  values = {
    "GAS_RELEASED": 0,
    "CRUISE_ACTIVE": 0,
    "ACC_BRAKING": 0,
    "ACCEL_NET": 0,
    "CRUISE_STATE": 0,
    "CANCEL_REQ": 1,
  }
  return packer.make_can_msg("PCM_CRUISE", 0, values)


def create_fcw_command(packer, fcw):
  values = {
    "PCS_INDICATOR": 1,  # PCS turned off
    "FCW": fcw,
    "SET_ME_X20": 0x20,
    "SET_ME_X10": 0x10,
    "PCS_OFF": 1,
    "PCS_SENSITIVITY": 0,
  }
  return packer.make_can_msg("PCS_HUD", 0, values)


def create_ui_command(packer, steer, chime, left_line, right_line, left_lane_depart, right_lane_depart, enabled, stock_lkas_hud):
  values = {
    "TWO_BEEPS": chime,
    "LDA_ALERT": steer,
    "RIGHT_LINE": 3 if right_lane_depart else 1 if right_line else 2,
    "LEFT_LINE": 3 if left_lane_depart else 1 if left_line else 2,
    "BARRIERS": 1 if enabled else 0,

    # static signals
    "SET_ME_X02": 2,
    "SET_ME_X01": 1,
    "LKAS_STATUS": 1,
    "REPEATED_BEEPS": 0,
    "LANE_SWAY_FLD": 7,
    "LANE_SWAY_BUZZER": 0,
    "LANE_SWAY_WARNING": 0,
    "LDA_FRONT_CAMERA_BLOCKED": 0,
    "TAKE_CONTROL": 0,
    "LANE_SWAY_SENSITIVITY": 2,
    "LANE_SWAY_TOGGLE": 1,
    "LDA_ON_MESSAGE": 0,
    "LDA_MESSAGES": 0,
    "LDA_SA_TOGGLE": 1,
    "LDA_SENSITIVITY": 2,
    "LDA_UNAVAILABLE": 0,
    "LDA_MALFUNCTION": 0,
    "LDA_UNAVAILABLE_QUIET": 0,
    "ADJUSTING_CAMERA": 0,
    "LDW_EXIST": 1,
  }

  # lane sway functionality
  # not all cars have LKAS_HUD — update with camera values if available
  if len(stock_lkas_hud):
    values.update({s: stock_lkas_hud[s] for s in [
      "LANE_SWAY_FLD",
      "LANE_SWAY_BUZZER",
      "LANE_SWAY_WARNING",
      "LANE_SWAY_SENSITIVITY",
      "LANE_SWAY_TOGGLE",
    ]})

  return packer.make_can_msg("LKAS_HUD", 0, values)
