from selfdrive.car import dbc_dict
from cereal import car
Ecu = car.CarParams.Ecu

# Steer torque limits
class SteerLimitParams:
  STEER_MAX = 1500
  STEER_DELTA_UP = 10       # 1.5s time to peak torque
  STEER_DELTA_DOWN = 25     # always lower than 45 otherwise the Rav4 faults (Prius seems ok with 50)
  STEER_ERROR_MAX = 350     # max delta between torque cmd and torque motor

class CAR:
  PRIUS = "TOYOTA PRIUS 2017"
  RAV4H = "TOYOTA RAV4 HYBRID 2017"
  RAV4 = "TOYOTA RAV4 2017"
  COROLLA = "TOYOTA COROLLA 2017"
  LEXUS_RX = "LEXUS RX 350 2016"
  LEXUS_RXH = "LEXUS RX HYBRID 2017"
  LEXUS_RX_TSS2 = "LEXUS RX350 2020"
  CHR = "TOYOTA C-HR 2018"
  CHRH = "TOYOTA C-HR HYBRID 2018"
  CAMRY = "TOYOTA CAMRY 2018"
  CAMRYH = "TOYOTA CAMRY HYBRID 2018"
  HIGHLANDER = "TOYOTA HIGHLANDER 2017"
  HIGHLANDERH = "TOYOTA HIGHLANDER HYBRID 2018"
  AVALON = "TOYOTA AVALON 2016"
  RAV4_TSS2 = "TOYOTA RAV4 2019"
  COROLLA_TSS2 = "TOYOTA COROLLA TSS2 2019"
  COROLLAH_TSS2 = "TOYOTA COROLLA HYBRID TSS2 2019"
  LEXUS_ES_TSS2 = "LEXUS ES 2019"
  LEXUS_ESH_TSS2 = "LEXUS ES 300H 2019"
  SIENNA = "TOYOTA SIENNA XLE 2018"
  LEXUS_IS = "LEXUS IS300 2018"
  LEXUS_CTH = "LEXUS CT 200H 2018"
  RAV4H_TSS2 = "TOYOTA RAV4 HYBRID 2019"


# addr: (ecu, cars, bus, 1/freq*100, vl)
STATIC_MSGS = [
  (0x128, Ecu.dsu, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA, CAR.AVALON), 1,   3, b'\xf4\x01\x90\x83\x00\x37'),
  (0x128, Ecu.dsu, (CAR.HIGHLANDER, CAR.HIGHLANDERH, CAR.SIENNA, CAR.LEXUS_CTH), 1,   3, b'\x03\x00\x20\x00\x00\x52'),
  (0x141, Ecu.dsu, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA, CAR.HIGHLANDER, CAR.HIGHLANDERH, CAR.AVALON, CAR.SIENNA, CAR.LEXUS_CTH, CAR.LEXUS_RX), 1,   2, b'\x00\x00\x00\x46'),
  (0x160, Ecu.dsu, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA, CAR.HIGHLANDER, CAR.HIGHLANDERH, CAR.AVALON, CAR.SIENNA, CAR.LEXUS_CTH, CAR.LEXUS_RX), 1,   7, b'\x00\x00\x08\x12\x01\x31\x9c\x51'),
  (0x161, Ecu.dsu, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA, CAR.AVALON, CAR.LEXUS_RX), 1,   7, b'\x00\x1e\x00\x00\x00\x80\x07'),
  (0X161, Ecu.dsu, (CAR.HIGHLANDERH, CAR.HIGHLANDER, CAR.SIENNA, CAR.LEXUS_CTH), 1,  7, b'\x00\x1e\x00\xd4\x00\x00\x5b'),
  (0x283, Ecu.dsu, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA, CAR.HIGHLANDER, CAR.HIGHLANDERH, CAR.AVALON, CAR.SIENNA, CAR.LEXUS_CTH, CAR.LEXUS_RX), 0,   3, b'\x00\x00\x00\x00\x00\x00\x8c'),
  (0x2E6, Ecu.dsu, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH), 0,   3, b'\xff\xf8\x00\x08\x7f\xe0\x00\x4e'),
  (0x2E7, Ecu.dsu, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH), 0,   3, b'\xa8\x9c\x31\x9c\x00\x00\x00\x02'),
  (0x33E, Ecu.dsu, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH), 0,  20, b'\x0f\xff\x26\x40\x00\x1f\x00'),
  (0x344, Ecu.dsu, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA, CAR.HIGHLANDER, CAR.HIGHLANDERH, CAR.AVALON, CAR.SIENNA, CAR.LEXUS_CTH, CAR.LEXUS_RX), 0,   5, b'\x00\x00\x01\x00\x00\x00\x00\x50'),
  (0x365, Ecu.dsu, (CAR.PRIUS, CAR.LEXUS_RXH, CAR.HIGHLANDERH), 0,  20, b'\x00\x00\x00\x80\x03\x00\x08'),
  (0x365, Ecu.dsu, (CAR.RAV4, CAR.RAV4H, CAR.COROLLA, CAR.HIGHLANDER, CAR.AVALON, CAR.SIENNA, CAR.LEXUS_CTH, CAR.LEXUS_RX), 0,  20, b'\x00\x00\x00\x80\xfc\x00\x08'),
  (0x366, Ecu.dsu, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.HIGHLANDERH), 0,  20, b'\x00\x00\x4d\x82\x40\x02\x00'),
  (0x366, Ecu.dsu, (CAR.RAV4, CAR.COROLLA, CAR.HIGHLANDER, CAR.AVALON, CAR.SIENNA, CAR.LEXUS_CTH, CAR.LEXUS_RX), 0,  20, b'\x00\x72\x07\xff\x09\xfe\x00'),
  (0x470, Ecu.dsu, (CAR.PRIUS, CAR.LEXUS_RXH), 1, 100, b'\x00\x00\x02\x7a'),
  (0x470, Ecu.dsu, (CAR.HIGHLANDER, CAR.HIGHLANDERH, CAR.RAV4H, CAR.SIENNA, CAR.LEXUS_CTH), 1,  100, b'\x00\x00\x01\x79'),
  (0x4CB, Ecu.dsu, (CAR.PRIUS, CAR.RAV4H, CAR.LEXUS_RXH, CAR.RAV4, CAR.COROLLA, CAR.HIGHLANDERH, CAR.HIGHLANDER, CAR.AVALON, CAR.SIENNA, CAR.LEXUS_CTH, CAR.LEXUS_RX), 0, 100, b'\x0c\x00\x00\x00\x00\x00\x00\x00'),

  (0x292, Ecu.apgs, (CAR.PRIUS), 0,   3, b'\x00\x00\x00\x00\x00\x00\x00\x9e'),
  (0x32E, Ecu.apgs, (CAR.PRIUS), 0,  20, b'\x00\x00\x00\x00\x00\x00\x00\x00'),
  (0x396, Ecu.apgs, (CAR.PRIUS), 0, 100, b'\xBD\x00\x00\x00\x60\x0F\x02\x00'),
  (0x43A, Ecu.apgs, (CAR.PRIUS), 0, 100, b'\x84\x00\x00\x00\x00\x00\x00\x00'),
  (0x43B, Ecu.apgs, (CAR.PRIUS), 0, 100, b'\x00\x00\x00\x00\x00\x00\x00\x00'),
  (0x497, Ecu.apgs, (CAR.PRIUS), 0, 100, b'\x00\x00\x00\x00\x00\x00\x00\x00'),
  (0x4CC, Ecu.apgs, (CAR.PRIUS), 0, 100, b'\x0D\x00\x00\x00\x00\x00\x00\x00'),
]

ECU_FINGERPRINT = {
  Ecu.fwdCamera: [0x2e4],   # steer torque cmd
  Ecu.dsu: [0x343],   # accel cmd
  Ecu.apgs: [0x835],  # angle cmd
}


FINGERPRINTS = {

  CAR.COROLLA_TSS2: [
  # hatch 2019 6MT
  {
    36: 8, 37: 8, 114: 5, 170: 8, 180: 8, 186: 4, 401: 8, 426: 6, 452: 8, 464: 8, 466: 8, 467: 8, 544: 4, 550: 8, 552: 4, 562: 6, 608: 8, 610: 8, 643: 7, 705: 8, 728: 8, 740: 5, 742: 8, 743: 8, 761: 8, 764: 8, 765: 8, 800: 8, 810: 2, 812: 8, 824: 8, 829: 2, 830: 7, 835: 8, 836: 8, 865: 8, 869: 7, 870: 7, 871: 2, 877: 8, 881: 8, 896: 8, 898: 8, 900: 6, 902: 6, 905: 8, 921: 8, 933: 8, 934: 8, 935: 8, 944: 8, 945: 8, 951: 8, 955: 8, 956: 8, 976: 1, 998: 5, 999: 7, 1000: 8, 1001: 8, 1002: 8, 1014: 8, 1017: 8, 1020: 8, 1041: 8, 1042: 8, 1044: 8, 1056: 8, 1059: 1, 1076: 8, 1077: 8, 1114: 8, 1161: 8, 1162: 8, 1163: 8, 1164: 8, 1165: 8, 1166: 8, 1167: 8, 1172: 8, 1235: 8, 1237: 8, 1279: 8, 1541: 8, 1552: 8, 1553: 8, 1556: 8, 1557: 8, 1568: 8, 1570: 8, 1571: 8, 1572: 8, 1592: 8, 1595: 8, 1649: 8, 1745: 8, 1775: 8, 1779: 8, 1786: 8, 1787: 8, 1788: 8, 1789: 8, 1808: 8, 1809: 8, 1816: 8, 1840: 8, 1848: 8, 1904: 8, 1912: 8, 1940: 8, 1941: 8, 1948: 8, 1949: 8, 1952: 8, 1960: 8, 1973: 8, 1981: 8, 1986: 8, 1990: 8, 1994: 8, 1998: 8, 2004: 8, 2012: 8
  }],
}

FW_VERSIONS = {
  CAR.AVALON: {
    (Ecu.esp, 0x7b0, None): [b'F152607060\x00\x00\x00\x00\x00\x00'],
    (Ecu.dsu, 0x791, None): [b'881510705200\x00\x00\x00\x00'],
    (Ecu.eps, 0x7a1, None): [b'8965B41051\x00\x00\x00\x00\x00\x00'],
    (Ecu.engine, 0x7e0, None): [b'\x0230721200\x00\x00\x00\x00\x00\x00\x00\x00A0C01000\x00\x00\x00\x00\x00\x00\x00\x00'],
    (Ecu.fwdRadar, 0x750, 0xf): [b'8821F4702100\x00\x00\x00\x00'],
    (Ecu.fwdCamera, 0x750, 0x6d): [b'8646F0703000\x00\x00\x00\x00'],
  },
  CAR.CAMRY: {
    (Ecu.engine, 0x700, None): [
      b'\x018966333P4200\x00\x00\x00\x00',
      b'\x018966333P4300\x00\x00\x00\x00',
      b'\x018966333P4400\x00\x00\x00\x00',
      b'\x018966333P4500\x00\x00\x00\x00',
      b'\x018966333P4700\x00\x00\x00\x00',
    ],
    (Ecu.dsu, 0x791, None): [
      b'8821F0607200    ',
      b'8821F0601300    ',
      b'8821F0603300    ',
    ],
    (Ecu.esp, 0x7b0, None): [
      b'F152606210\x00\x00\x00\x00\x00\x00',
      b'F152606230\x00\x00\x00\x00\x00\x00',
      b'F152606290\x00\x00\x00\x00\x00\x00',
      b'F152633540\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.eps, 0x7a1, None): [b'8965B33540\x00\x00\x00\x00\x00\x00'],
    (Ecu.fwdRadar, 0x750, 0xf): [  # Same as 0x791
      b'8821F0601300    ',
      b'8821F0603300    ',
      b'8821F0607200    ',
    ],
    (Ecu.fwdCamera, 0x750, 0x6d): [
      b'8646F0601200    ',
      b'8646F0601300    ',
      b'8646F0603400    ',
    ],
  },
  CAR.CAMRYH: {
    (Ecu.engine, 0x700, None): [
      b'\x028966306B2100\x00\x00\x00\x00897CF3302002\x00\x00\x00\x00',
      b'\x028966306N8200\x00\x00\x00\x00897CF3302002\x00\x00\x00\x00',
      b'\x028966306R5000\x00\x00\x00\x00897CF3302002\x00\x00\x00\x00',
      b'\x028966306R6000\x00\x00\x00\x00897CF3302002\x00\x00\x00\x00',
    ],
    (Ecu.esp, 0x7b0, None): [
      b'F152633712\x00\x00\x00\x00\x00\x00',
      b'F152633713\x00\x00\x00\x00\x00\x00',
      b'F152633B51\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.dsu, 0x791, None): [
      b'8821F0601200    ',
      b'8821F0601300    ',
      b'8821F0607200    ',
    ],
    (Ecu.eps, 0x7a1, None): [b'8965B33540\x00\x00\x00\x00\x00\x00'],
    (Ecu.fwdRadar, 0x750, 0xf): [  # Same as 0x791
      b'8821F0601200    ',
      b'8821F0601300    ',
      b'8821F0607200    ',
    ],
    (Ecu.fwdCamera, 0x750, 0x6d): [
      b'8646F0601200    ',
      b'8646F0601300    ',
      b'8646F0605000    ',
    ],
  },
  CAR.COROLLA: {
    (Ecu.engine, 0x7e0, None): [
      b'\x01896630E88000\x00\x00\x00\x00',
      b'\x0230ZC2100\x00\x00\x00\x00\x00\x00\x00\x0050212000\x00\x00\x00\x00\x00\x00\x00\x00',
      b'\x0230ZC2200\x00\x00\x00\x00\x00\x00\x00\x0050212000\x00\x00\x00\x00\x00\x00\x00\x00',
      b'\x0230ZC2300\x00\x00\x00\x00\x00\x00\x00\x0050212000\x00\x00\x00\x00\x00\x00\x00\x00',
      b'\x0230ZC3000\x00\x00\x00\x00\x00\x00\x00\x0050212000\x00\x00\x00\x00\x00\x00\x00\x00',
      b'\x0230ZC3200\x00\x00\x00\x00\x00\x00\x00\x0050212000\x00\x00\x00\x00\x00\x00\x00\x00',
      b'\x0230ZC3300\x00\x00\x00\x00\x00\x00\x00\x0050212000\x00\x00\x00\x00\x00\x00\x00\x00',
      b'\x0330ZC1200\x00\x00\x00\x00\x00\x00\x00\x0050212000\x00\x00\x00\x00\x00\x00\x00\x00895231203202\x00\x00\x00\x00',
    ],
    (Ecu.dsu, 0x791, None): [
      b'881510201100\x00\x00\x00\x00',
      b'881510201200\x00\x00\x00\x00',
    ],
    (Ecu.esp, 0x7b0, None): [
      b'F152602190\x00\x00\x00\x00\x00\x00',
      b'F152602191\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.eps, 0x7a1, None): [
      b'8965B02181\x00\x00\x00\x00\x00\x00',
      b'8965B02191\x00\x00\x00\x00\x00\x00',
      b'8965B48150\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.fwdRadar, 0x750, 0xf): [
      b'8821F4702100\x00\x00\x00\x00',
      b'8821F4702300\x00\x00\x00\x00',
    ],
    (Ecu.fwdCamera, 0x750, 0x6d): [
      b'8646F0201101\x00\x00\x00\x00',
      b'8646F0201200\x00\x00\x00\x00',
      b'8646F0E01300\x00\x00\x00\x00',
    ],
  },
  CAR.COROLLA_TSS2: {
    (Ecu.engine, 0x700, None): [
      b'\x01896630ZG5000\x00\x00\x00\x00',
      b'\x01896630ZG5100\x00\x00\x00\x00',
      b'\x01896630ZG5200\x00\x00\x00\x00',
      b'\x01896630ZQ5000\x00\x00\x00\x00',
      b'\x018966312L8000\x00\x00\x00\x00',
      b'\x018966312P9000\x00\x00\x00\x00',
      b'\x018966312P9100\x00\x00\x00\x00',
      b'\x018966312P9200\x00\x00\x00\x00',
      b'\x018966312R1000\x00\x00\x00\x00',
      b'\x018966312R1100\x00\x00\x00\x00',
      b'\x018966312R3100\x00\x00\x00\x00',
    ],
    (Ecu.engine, 0x7e0, None): [
      b'\x03312N6000\x00\x00\x00\x00\x00\x00\x00\x00A0202000\x00\x00\x00\x00\x00\x00\x00\x00895231203202\x00\x00\x00\x00',
      b'\x03312N6000\x00\x00\x00\x00\x00\x00\x00\x00A0202000\x00\x00\x00\x00\x00\x00\x00\x00895231203302\x00\x00\x00\x00',
      b'\x03312N6100\x00\x00\x00\x00\x00\x00\x00\x00A0202000\x00\x00\x00\x00\x00\x00\x00\x00895231203302\x00\x00\x00\x00',
    ],
    (Ecu.eps, 0x7a1, None): [
      b'8965B12361\x00\x00\x00\x00\x00\x00',
      b'\x018965B12350\x00\x00\x00\x00\x00\x00',
      b'\x018965B12500\x00\x00\x00\x00\x00\x00',
      b'\x018965B12530\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.esp, 0x7b0, None): [
      b'F152602191\x00\x00\x00\x00\x00\x00',
      b'\x01F152602280\x00\x00\x00\x00\x00\x00',
      b'\x01F152602560\x00\x00\x00\x00\x00\x00',
      b'\x01F152612641\x00\x00\x00\x00\x00\x00',
      b'\x01F152612B10\x00\x00\x00\x00\x00\x00',
      b'\x01F152612B60\x00\x00\x00\x00\x00\x00',
      b'\x01F152612B90\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.fwdRadar, 0x750, 0xf): [
      b'\x018821F3301100\x00\x00\x00\x00',
      b'\x018821F3301200\x00\x00\x00\x00',
      b'\x018821F3301300\x00\x00\x00\x00',
      b'\x018821F3301400\x00\x00\x00\x00',
    ],
    (Ecu.fwdCamera, 0x750, 0x6d): [
      b'\x028646F12010D0\x00\x00\x00\x008646G26011A0\x00\x00\x00\x00',
      b'\x028646F1201100\x00\x00\x00\x008646G26011A0\x00\x00\x00\x00',
      b'\x028646F1201200\x00\x00\x00\x008646G26011A0\x00\x00\x00\x00',
      b'\x028646F1202000\x00\x00\x00\x008646G2601200\x00\x00\x00\x00',
    ],
  },
  CAR.COROLLAH_TSS2: {
    (Ecu.engine, 0x700, None): [
      b'\x018966342M5000\x00\x00\x00\x00',
      b'\x02896630ZQ3000\x00\x00\x00\x008966A4703000\x00\x00\x00\x00',
      b'\x02896630ZR2000\x00\x00\x00\x008966A4703000\x00\x00\x00\x00',
      b'\x028966312Q4000\x00\x00\x00\x008966A4703000\x00\x00\x00\x00',
      b'\x038966312N1000\x00\x00\x00\x008966A4703000\x00\x00\x00\x00897CF1203001\x00\x00\x00\x00',
    ],
    (Ecu.eps, 0x7a1, None): [
      b'8965B12361\x00\x00\x00\x00\x00\x00',
      b'8965B12451\x00\x00\x00\x00\x00\x00',
      b'8965B42170\x00\x00\x00\x00\x00\x00',
      b'\x018965B12350\x00\x00\x00\x00\x00\x00',
      b'\x018965B12470\x00\x00\x00\x00\x00\x00',
      b'\x018965B12500\x00\x00\x00\x00\x00\x00',
      b'\x018965B12530\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.esp, 0x7b0, None): [
      b'F152612590\x00\x00\x00\x00\x00\x00',
      b'F152612691\x00\x00\x00\x00\x00\x00',
      b'F152612700\x00\x00\x00\x00\x00\x00',
      b'F152612800\x00\x00\x00\x00\x00\x00',
      b'F152612840\x00\x00\x00\x00\x00\x00',
      b'F152642540\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.fwdRadar, 0x750, 0xf): [
      b'\x018821F3301200\x00\x00\x00\x00',
      b'\x018821F3301300\x00\x00\x00\x00',
      b'\x018821F3301400\x00\x00\x00\x00',
    ],
    (Ecu.fwdCamera, 0x750, 0x6d): [
      b'\x028646F1201100\x00\x00\x00\x008646G26011A0\x00\x00\x00\x00',
      b'\x028646F1202000\x00\x00\x00\x008646G2601200\x00\x00\x00\x00',
      b'\x028646F4203400\x00\x00\x00\x008646G2601200\x00\x00\x00\x00',
    ],
  },
  CAR.HIGHLANDER: {
    (Ecu.engine, 0x700, None): [
      b'\x01896630E43100\x00\x00\x00\x00',
      b'\x01896630E45200\x00\x00\x00\x00',
      b'\x01896630E83000\x00\x00\x00\x00',
      b'\x01896630E84000\x00\x00\x00\x00',
      b'\x01896630E85000\x00\x00\x00\x00',
      b'\x01896630E88000\x00\x00\x00\x00',
    ],
    (Ecu.eps, 0x7a1, None): [
      b'8965B48140\x00\x00\x00\x00\x00\x00',
      b'8965B48150\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.esp, 0x7b0, None): [b'F15260E011\x00\x00\x00\x00\x00\x00'],
    (Ecu.dsu, 0x791, None): [
      b'881510E01100\x00\x00\x00\x00',
      b'881510E01200\x00\x00\x00\x00',
    ],
    (Ecu.fwdRadar, 0x750, 0xf): [
      b'8821F4702100\x00\x00\x00\x00',
      b'8821F4702300\x00\x00\x00\x00',
    ],
    (Ecu.fwdCamera, 0x750, 0x6d): [
      b'8646F0E01200\x00\x00\x00\x00',
      b'8646F0E01300\x00\x00\x00\x00',
    ],
  },
  CAR.HIGHLANDERH: {
    (Ecu.eps, 0x7a1, None): [b'8965B48160\x00\x00\x00\x00\x00\x00'],
    (Ecu.esp, 0x7b0, None): [b'F152648541\x00\x00\x00\x00\x00\x00'],
    (Ecu.engine, 0x7e0, None): [b'\x0230E40000\x00\x00\x00\x00\x00\x00\x00\x00A4802000\x00\x00\x00\x00\x00\x00\x00\x00'],
    (Ecu.fwdRadar, 0x750, 0xf): [b'8821F4702100\x00\x00\x00\x00'],
    (Ecu.fwdCamera, 0x750, 0x6d): [b'8646F0E01200\x00\x00\x00\x00'],
  },
  CAR.LEXUS_IS: {
    (Ecu.engine, 0x700, None): [b'\x018966353Q2300\x00\x00\x00\x00'],
    (Ecu.esp, 0x7b0, None): [b'F152653330\x00\x00\x00\x00\x00\x00'],
    (Ecu.dsu, 0x791, None): [b'881515306400\x00\x00\x00\x00'],
    (Ecu.eps, 0x7a1, None): [b'8965B53271\x00\x00\x00\x00\x00\x00'],
    (Ecu.fwdRadar, 0x750, 0xf): [b'8821F4702300\x00\x00\x00\x00'],
    (Ecu.fwdCamera, 0x750, 0x6d): [b'8646F5301400\x00\x00\x00\x00'],
  },
  CAR.PRIUS: {
    (Ecu.engine, 0x700, None): [
      b'\x02896634761000\x00\x00\x00\x008966A4703000\x00\x00\x00\x00',
      b'\x02896634761100\x00\x00\x00\x008966A4703000\x00\x00\x00\x00',
      b'\x02896634763000\x00\x00\x00\x008966A4703000\x00\x00\x00\x00',
      b'\x02896634769100\x00\x00\x00\x008966A4703000\x00\x00\x00\x00',
      b'\x02896634774000\x00\x00\x00\x008966A4703000\x00\x00\x00\x00',
      b'\x02896634774100\x00\x00\x00\x008966A4703000\x00\x00\x00\x00',
      b'\x02896634774200\x00\x00\x00\x008966A4703000\x00\x00\x00\x00',
      b'\x02896634782000\x00\x00\x00\x008966A4703000\x00\x00\x00\x00',
      b'\x03896634759200\x00\x00\x00\x008966A4703000\x00\x00\x00\x00897CF4701003\x00\x00\x00\x00',
      b'\x03896634759300\x00\x00\x00\x008966A4703000\x00\x00\x00\x00897CF4701004\x00\x00\x00\x00',
      b'\x03896634760000\x00\x00\x00\x008966A4703000\x00\x00\x00\x00897CF4701002\x00\x00\x00\x00',
      b'\x03896634760200\x00\x00\x00\x008966A4703000\x00\x00\x00\x00897CF4701003\x00\x00\x00\x00',
      b'\x03896634760200\x00\x00\x00\x008966A4703000\x00\x00\x00\x00897CF4701004\x00\x00\x00\x00',
      b'\x03896634768000\x00\x00\x00\x008966A4703000\x00\x00\x00\x00897CF4703001\x00\x00\x00\x00',
      b'\x03896634768000\x00\x00\x00\x008966A4703000\x00\x00\x00\x00897CF4703002\x00\x00\x00\x00',
      b'\x03896634768100\x00\x00\x00\x008966A4703000\x00\x00\x00\x00897CF4703002\x00\x00\x00\x00',
      b'\x03896634785000\x00\x00\x00\x008966A4703000\x00\x00\x00\x00897CF4705001\x00\x00\x00\x00',
      b'\x03896634786000\x00\x00\x00\x008966A4703000\x00\x00\x00\x00897CF4710001\x00\x00\x00\x00',
      b'\x03896634789000\x00\x00\x00\x008966A4703000\x00\x00\x00\x00897CF4703002\x00\x00\x00\x00',
      b'\x038966347A3000\x00\x00\x00\x008966A4703000\x00\x00\x00\x00897CF4707001\x00\x00\x00\x00',
    ],
    (Ecu.eps, 0x7a1, None): [
      b'8965B47021\x00\x00\x00\x00\x00\x00',
      b'8965B47022\x00\x00\x00\x00\x00\x00',
      b'8965B47023\x00\x00\x00\x00\x00\x00',
      b'8965B47050\x00\x00\x00\x00\x00\x00',
      b'8965B47060\x00\x00\x00\x00\x00\x00',  # Think this the EPS with good angle sensor
    ],
    (Ecu.esp, 0x7b0, None): [
      b'F152647290\x00\x00\x00\x00\x00\x00',
      b'F152647310\x00\x00\x00\x00\x00\x00',
      b'F152647414\x00\x00\x00\x00\x00\x00',
      b'F152647415\x00\x00\x00\x00\x00\x00',
      b'F152647416\x00\x00\x00\x00\x00\x00',
      b'F152647417\x00\x00\x00\x00\x00\x00',
      b'F152647490\x00\x00\x00\x00\x00\x00',
      b'F152647684\x00\x00\x00\x00\x00\x00',
      b'F152647862\x00\x00\x00\x00\x00\x00',
      b'F152647863\x00\x00\x00\x00\x00\x00',
      b'F152647864\x00\x00\x00\x00\x00\x00',
      b'F152647865\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.dsu, 0x791, None): [
      b'881514702300\x00\x00\x00\x00',
      b'881514703100\x00\x00\x00\x00',
      b'881514704100\x00\x00\x00\x00',
      b'881514706000\x00\x00\x00\x00',
    ],
    (Ecu.fwdRadar, 0x750, 0xf): [
      b'8821F4702000\x00\x00\x00\x00',
      b'8821F4702100\x00\x00\x00\x00',
      b'8821F4702300\x00\x00\x00\x00',
    ],
    (Ecu.fwdCamera, 0x750, 0x6d): [
      b'8646F4201200\x00\x00\x00\x00',
      b'8646F4701300\x00\x00\x00\x00',
      b'8646F4702001\x00\x00\x00\x00',
      b'8646F4702100\x00\x00\x00\x00',
      b'8646F4702200\x00\x00\x00\x00',
      b'8646F4705000\x00\x00\x00\x00',
      b'8646F4705200\x00\x00\x00\x00',
    ],
  },
  CAR.RAV4: {
    (Ecu.engine, 0x7e0, None): [
      b'\x02342Q1100\x00\x00\x00\x00\x00\x00\x00\x0054212000\x00\x00\x00\x00\x00\x00\x00\x00',
      b'\x02342Q1300\x00\x00\x00\x00\x00\x00\x00\x0054212000\x00\x00\x00\x00\x00\x00\x00\x00',
      b'\x02342Q2000\x00\x00\x00\x00\x00\x00\x00\x0054213000\x00\x00\x00\x00\x00\x00\x00\x00',
      b'\x02342Q2100\x00\x00\x00\x00\x00\x00\x00\x0054213000\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.eps, 0x7a1, None): [
      b'8965B42082\x00\x00\x00\x00\x00\x00',
      b'8965B42083\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.esp, 0x7b0, None): [
      b'F15260R103\x00\x00\x00\x00\x00\x00',
      b'F152642493\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.dsu, 0x791, None): [
      b'881514201300\x00\x00\x00\x00',
      b'881514201400\x00\x00\x00\x00',
    ],
    (Ecu.fwdRadar, 0x750, 0xf): [
      b'8821F4702000\x00\x00\x00\x00',
      b'8821F4702100\x00\x00\x00\x00',
      b'8821F4702300\x00\x00\x00\x00',
    ],
    (Ecu.fwdCamera, 0x750, 0x6d): [
      b'8646F4201200\x00\x00\x00\x00',
      b'8646F4202001\x00\x00\x00\x00',
      b'8646F4202100\x00\x00\x00\x00',
    ],
  },
  CAR.RAV4H: {
    (Ecu.engine, 0x7e0, None): [
      b'\x02342N9000\x00\x00\x00\x00\x00\x00\x00\x00A4701000\x00\x00\x00\x00\x00\x00\x00\x00',
      b'\x02342N9100\x00\x00\x00\x00\x00\x00\x00\x00A4701000\x00\x00\x00\x00\x00\x00\x00\x00',
      b'\x02342P0000\x00\x00\x00\x00\x00\x00\x00\x00A4701000\x00\x00\x00\x00\x00\x00\x00\x00',
      b'\x02342Q2000\x00\x00\x00\x00\x00\x00\x00\x0054213000\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.eps, 0x7a1, None): [
      b'8965B42103\x00\x00\x00\x00\x00\x00',
      b'8965B42162\x00\x00\x00\x00\x00\x00',
      b'8965B42163\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.esp, 0x7b0, None): [
      b'F152642090\x00\x00\x00\x00\x00\x00',
      b'F152642120\x00\x00\x00\x00\x00\x00',
      b'F152642400\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.fwdRadar, 0x750, 0xf): [
      b'8821F4702000\x00\x00\x00\x00',
      b'8821F4702100\x00\x00\x00\x00',
      b'8821F4702300\x00\x00\x00\x00',
    ],
    (Ecu.fwdCamera, 0x750, 0x6d): [
      b'8646F4201100\x00\x00\x00\x00',
      b'8646F4201200\x00\x00\x00\x00',
      b'8646F4202001\x00\x00\x00\x00',
      b'8646F4202100\x00\x00\x00\x00',
      b'8646F4204000\x00\x00\x00\x00',
    ],
  },
  CAR.RAV4_TSS2: {
    (Ecu.engine, 0x700, None): [
      b'\x018966333Q6200\x00\x00\x00\x00',
      b'\x018966342E2000\x00\x00\x00\x00',
      b'\x018966342M8000\x00\x00\x00\x00',
      b'\x018966342T1000\x00\x00\x00\x00',
      b'\x018966342T6000\x00\x00\x00\x00',
      b'\x018966342V3100\x00\x00\x00\x00',
      b'\x018966342X5000\x00\x00\x00\x00',
      b'\x01896634A05000\x00\x00\x00\x00',
      b'\x01896634A22000\x00\x00\x00\x00',
      b'\x01F152642551\x00\x00\x00\x00\x00\x00',
      b'\x028966342Y8000\x00\x00\x00\x00897CF1201001\x00\x00\x00\x00',
    ],
    (Ecu.esp, 0x7b0, None): [
      b'F152606230\x00\x00\x00\x00\x00\x00',
      b'F152642520\x00\x00\x00\x00\x00\x00',
      b'\x01F15260R210\x00\x00\x00\x00\x00\x00',
      b'\x01F15260R220\x00\x00\x00\x00\x00\x00',
      b'\x01F152642551\x00\x00\x00\x00\x00\x00',
      b'\x01F152642561\x00\x00\x00\x00\x00\x00',
      b'\x01F152642710\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.eps, 0x7a1, None): [
      b'8965B33540\x00\x00\x00\x00\x00\x00',
      b'8965B42170\x00\x00\x00\x00\x00\x00',
      b'8965B42171\x00\x00\x00\x00\x00\x00',
      b'\x028965B0R01200\x00\x00\x00\x008965B0R02200\x00\x00\x00\x00',
    ],
    (Ecu.fwdRadar, 0x750, 0xf): [
      b'8821F0607200    ',
      b'\x018821F3301100\x00\x00\x00\x00',
      b'\x018821F3301200\x00\x00\x00\x00',
      b'\x018821F3301300\x00\x00\x00\x00',
      b'\x018821F3301400\x00\x00\x00\x00',
    ],
    (Ecu.fwdCamera, 0x750, 0x6d): [
      b'8646F0605000    ',
      b'\x028646F4203200\x00\x00\x00\x008646G26011A0\x00\x00\x00\x00',
      b'\x028646F4203300\x00\x00\x00\x008646G26011A0\x00\x00\x00\x00',
      b'\x028646F4203400\x00\x00\x00\x008646G2601200\x00\x00\x00\x00',
      b'\x028646F4203500\x00\x00\x00\x008646G2601200\x00\x00\x00\x00',
    ],
  },
  CAR.RAV4H_TSS2: {
    (Ecu.engine, 0x700, None): [
      b'\x018966342X6000\x00\x00\x00\x00',
      b'\x028966342W4001\x00\x00\x00\x00897CF1203001\x00\x00\x00\x00',
      b'\x02896634A23001\x00\x00\x00\x00897CF1203001\x00\x00\x00\x00',
    ],
    (Ecu.esp, 0x7b0, None): [
      b'F152642291\x00\x00\x00\x00\x00\x00',
      b'F152642531\x00\x00\x00\x00\x00\x00',
      b'F152642532\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.eps, 0x7a1, None): [
      b'8965B42170\x00\x00\x00\x00\x00\x00',
      b'8965B42171\x00\x00\x00\x00\x00\x00',
      b'8965B42181\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.fwdRadar, 0x750, 0xf): [
      b'\x018821F3301200\x00\x00\x00\x00',
      b'\x018821F3301300\x00\x00\x00\x00',
      b'\x018821F3301400\x00\x00\x00\x00',
    ],
    (Ecu.fwdCamera, 0x750, 0x6d): [
      b'\x028646F4203300\x00\x00\x00\x008646G26011A0\x00\x00\x00\x00',
      b'\x028646F4203400\x00\x00\x00\x008646G2601200\x00\x00\x00\x00',
      b'\x028646F4203500\x00\x00\x00\x008646G2601200\x00\x00\x00\x00',
    ],
  },
  CAR.LEXUS_ES_TSS2: {
    (Ecu.engine, 0x700, None): [b'\x018966333T5100\x00\x00\x00\x00'],
    (Ecu.esp, 0x7b0, None): [b'\x01F152606281\x00\x00\x00\x00\x00\x00'],
    (Ecu.eps, 0x7a1, None): [b'8965B33252\x00\x00\x00\x00\x00\x00'],
    (Ecu.fwdRadar, 0x750, 0xf): [b'\x018821F3301200\x00\x00\x00\x00'],
    (Ecu.fwdCamera, 0x750, 0x6d): [b'\x028646F3303200\x00\x00\x00\x008646G26011A0\x00\x00\x00\x00'],
  },
  CAR.LEXUS_IS: {
    (Ecu.engine, 0x700, None): [b'\x018966353Q2300\x00\x00\x00\x00'],
    (Ecu.dsu, 0x791, None): [b'881515306400\x00\x00\x00\x00'],
    (Ecu.eps, 0x7a1, None): [b'8965B53271\x00\x00\x00\x00\x00\x00'],
    (Ecu.fwdRadar, 0x750, 0xf): [b'8821F4702300\x00\x00\x00\x00'],
    (Ecu.fwdCamera, 0x750, 0x6d): [b'8646F5301400\x00\x00\x00\x00'],
  },
  CAR.SIENNA: {
    (Ecu.engine, 0x700, None): [b'\x01896630832100\x00\x00\x00\x00'],
    (Ecu.eps, 0x7a1, None): [b'8965B45070\x00\x00\x00\x00\x00\x00'],
    (Ecu.fwdRadar, 0x750, 0xf): [b'8821F4702100\x00\x00\x00\x00'],
    (Ecu.fwdCamera, 0x750, 0x6d): [b'8646F0801100\x00\x00\x00\x00'],
  },
  CAR.LEXUS_RXH: {
    (Ecu.engine, 0x7e0, None): [
      b'\x02348Q4000\x00\x00\x00\x00\x00\x00\x00\x00A4802000\x00\x00\x00\x00\x00\x00\x00\x00',
      b'\x02348T1100\x00\x00\x00\x00\x00\x00\x00\x00A4802000\x00\x00\x00\x00\x00\x00\x00\x00',
      b'\x02348Z3000\x00\x00\x00\x00\x00\x00\x00\x00A4802000\x00\x00\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.esp, 0x7b0, None): [
      b'F152648501\x00\x00\x00\x00\x00\x00',
      b'F152648A30\x00\x00\x00\x00\x00\x00',
      b'F152648361\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.dsu, 0x791, None): [
      b'881514811300\x00\x00\x00\x00',
      b'881514811700\x00\x00\x00\x00',
    ],
    (Ecu.eps, 0x7a1, None): [
      b'8965B0E011\x00\x00\x00\x00\x00\x00',
      b'8965B0E012\x00\x00\x00\x00\x00\x00',
      b'8965B48112\x00\x00\x00\x00\x00\x00',
    ],
    (Ecu.fwdRadar, 0x750, 0xf): [
      b'8821F4701000\x00\x00\x00\x00',
      b'8821F4701300\x00\x00\x00\x00',
    ],
    (Ecu.fwdCamera, 0x750, 0x6d): [
      b'8646F4801200\x00\x00\x00\x00',
      b'8646F4802200\x00\x00\x00\x00',
      b'8646F4809000\x00\x00\x00\x00',
    ],
  },
}

STEER_THRESHOLD = 100

DBC = {
  CAR.RAV4H: dbc_dict('toyota_rav4_hybrid_2017_pt_generated', 'toyota_adas'),
  CAR.RAV4: dbc_dict('toyota_rav4_2017_pt_generated', 'toyota_adas'),
  CAR.PRIUS: dbc_dict('toyota_prius_2017_pt_generated', 'toyota_adas'),
  CAR.COROLLA: dbc_dict('toyota_corolla_2017_pt_generated', 'toyota_adas'),
  CAR.LEXUS_RX: dbc_dict('lexus_rx_350_2016_pt_generated', 'toyota_adas'),
  CAR.LEXUS_RXH: dbc_dict('lexus_rx_hybrid_2017_pt_generated', 'toyota_adas'),
  CAR.LEXUS_RX_TSS2: dbc_dict('toyota_nodsu_pt_generated', 'toyota_tss2_adas'),
  CAR.CHR: dbc_dict('toyota_nodsu_pt_generated', 'toyota_adas'),
  CAR.CHRH: dbc_dict('toyota_nodsu_hybrid_pt_generated', 'toyota_adas'),
  CAR.CAMRY: dbc_dict('toyota_nodsu_pt_generated', 'toyota_adas'),
  CAR.CAMRYH: dbc_dict('toyota_camry_hybrid_2018_pt_generated', 'toyota_adas'),
  CAR.HIGHLANDER: dbc_dict('toyota_highlander_2017_pt_generated', 'toyota_adas'),
  CAR.HIGHLANDERH: dbc_dict('toyota_highlander_hybrid_2018_pt_generated', 'toyota_adas'),
  CAR.AVALON: dbc_dict('toyota_avalon_2017_pt_generated', 'toyota_adas'),
  CAR.RAV4_TSS2: dbc_dict('toyota_nodsu_pt_generated', 'toyota_tss2_adas'),
  CAR.COROLLA_TSS2: dbc_dict('toyota_nodsu_pt_generated', 'toyota_tss2_adas'),
  CAR.COROLLAH_TSS2: dbc_dict('toyota_nodsu_hybrid_pt_generated', 'toyota_tss2_adas'),
  CAR.LEXUS_ES_TSS2: dbc_dict('toyota_nodsu_pt_generated', 'toyota_tss2_adas'),
  CAR.LEXUS_ESH_TSS2: dbc_dict('toyota_nodsu_hybrid_pt_generated', 'toyota_tss2_adas'),
  CAR.SIENNA: dbc_dict('toyota_sienna_xle_2018_pt_generated', 'toyota_adas'),
  CAR.LEXUS_IS: dbc_dict('lexus_is_2018_pt_generated', 'toyota_adas'),
  CAR.LEXUS_CTH: dbc_dict('lexus_ct200h_2018_pt_generated', 'toyota_adas'),
  CAR.RAV4H_TSS2: dbc_dict('toyota_nodsu_hybrid_pt_generated', 'toyota_tss2_adas'),
}

NO_DSU_CAR = [CAR.CHR, CAR.CHRH, CAR.CAMRY, CAR.CAMRYH, CAR.RAV4_TSS2, CAR.COROLLA_TSS2, CAR.COROLLAH_TSS2, CAR.LEXUS_ES_TSS2, CAR.LEXUS_ESH_TSS2, CAR.RAV4H_TSS2, CAR.LEXUS_RX_TSS2]
TSS2_CAR = [CAR.RAV4_TSS2, CAR.COROLLA_TSS2, CAR.COROLLAH_TSS2, CAR.LEXUS_ES_TSS2, CAR.LEXUS_ESH_TSS2, CAR.RAV4H_TSS2, CAR.LEXUS_RX_TSS2]
NO_STOP_TIMER_CAR = [CAR.RAV4H, CAR.HIGHLANDERH, CAR.HIGHLANDER, CAR.RAV4_TSS2, CAR.COROLLA_TSS2, CAR.COROLLAH_TSS2, CAR.LEXUS_ES_TSS2, CAR.LEXUS_ESH_TSS2, CAR.SIENNA, CAR.RAV4H_TSS2, CAR.LEXUS_RX_TSS2]  # no resume button press required
