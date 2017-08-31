from __future__ import print_function, division
from sympy import symbols, simplify
from sympy.physics.mechanics import dynamicsymbols, ReferenceFrame, Point, inertia, RigidBody
# SymPy has a rich printing system. Here we initialize printing so that all of the mathematical equations are rendered in standard mathematical notation.
from sympy.physics.vector import init_vprinting
init_vprinting(use_latex='mathjax', pretty_print=False)


#___________________________________________________________________________________________________________________________________________________
# Functions

#___________________________________________________________________________________________________________________________________________________
# Reference Frames and Orientation

inertial_frame = ReferenceFrame('inertial_frame')
Chassis_frame = ReferenceFrame('Chassis_frame')
LSpdl_frame = ReferenceFrame('LSpdl_frame')
RSpdl_frame = ReferenceFrame('RSpdl_frame')
LUCA_frame = ReferenceFrame('LUCA_frame')
RUCA_frame = ReferenceFrame('RUCA_frame')
LLCA_frame = ReferenceFrame('LLCA_frame')
RLCA_frame = ReferenceFrame('RLCA_frame')
LTR_frame = ReferenceFrame('LTR_frame')
RTR_frame = ReferenceFrame('RTR_frame')
RP_frame = ReferenceFrame('RP_frame')
Hsg_frame = ReferenceFrame('Hsg_frame')
LBC_frame = ReferenceFrame('LBC_frame')
RBC_frame = ReferenceFrame('RBC_frame')
LUB_frame = ReferenceFrame('LUB_frame')
RUB_frame = ReferenceFrame('RUB_frame')
LLB_frame = ReferenceFrame('LLB_frame')
RLB_frame = ReferenceFrame('RLB_frame')
Jbar_frame = ReferenceFrame('Jbar_frame')
#LB_frame = ReferenceFrame('LB_frame')
LFT_frame = ReferenceFrame('LFT_frame')
RFT_frame = ReferenceFrame('RFT_frame')
LRT_frame = ReferenceFrame('LRT_frame')
RRT_frame = ReferenceFrame('RRT_frame')
LRTeth_frame = ReferenceFrame('LRTeth_frame')
RRTeth_frame = ReferenceFrame('RRTeth_frame')

#___________________________________________________________________________________________________________________________________________________
# Define the rotation angle symbols

thRPx = symbols('thRPx') ; thRPy = symbols('thRPy') ; thRPz = symbols('thRPz')
thLUCAy = symbols('thLUCAy') ; thLUCAz = symbols('thLUCAz')
thRUCAy = symbols('thRUCAy') ; thRUCAz = symbols('thRUCAz')
thLLCAy = symbols('thLLCAy') ; thLLCAz = symbols('thLLCAz')
thRLCAy = symbols('thRLCAy') ; thRLCAz = symbols('thRLCAz')
thLRTethy = symbols('thLRTethy') ; thRRTethy = symbols('thRRTethy')

thRoll, thPitch, thYaw = dynamicsymbols('thRoll, thPitch, thYaw')
thLUCAx, thLLCAx, thRUCAx, thRLCAx = dynamicsymbols('thLUCAx, thLLCAx, thRUCAx, thRLCAx')
thLTRx,thLTRy,thLTRz = dynamicsymbols('thLTRx,thLTRy,thLTRz')
thLSpdlx,thLSpdly,thLSpdlz = dynamicsymbols('thLSpdlx,thLSpdly,thLSpdlz')
thRTRx,thRTRy,thRTRz = dynamicsymbols('thRTRx,thRTRy,thRTRz')
thRSpdlx,thRSpdly,thRSpdlz = dynamicsymbols('thRSpdlx,thRSpdly,thRSpdlz')
thHsgx, thHsgy, thHsgz = dynamicsymbols('thHsgx, thHsgy, thHsgz')
thLBCy, thRBCy = dynamicsymbols('thLBCy, thRBCy')
thLUBx, thLUBy, thLUBz = dynamicsymbols('thLUBx, thLUBy, thLUBz')
thRUBx, thRUBy, thRUBz = dynamicsymbols('thRUBx, thRUBy, thRUBz')
thLLBx, thLLBy, thLLBz = dynamicsymbols('thLLBx, thLLBy, thLLBz')
thRLBx, thRLBy, thRLBz = dynamicsymbols('thRLBx, thRLBy, thRLBz')
thJbarx, thJbary, thJbarz = dynamicsymbols('thJbarx, thJbary, thJbarz')
thLFTy, thRFTy, thLRTy, thRRTy = dynamicsymbols('thLFTy, thRFTy, thLRTy, thRRTy')
transRPy = dynamicsymbols('transRPy') # Dynamic symbol for the translation of the rack and pinion

#___________________________________________________________________________________________________________________________________________________
# Orient the reference frames

Chassis_frame.orient(inertial_frame, 'Body', [thRoll,thPitch,thYaw],'XYZ')
RP_frame.orient(Chassis_frame,'Body',[thRPx,thRPy,thRPz],'XYZ')
LUCA_frame.orient(Chassis_frame, 'Body', [thLUCAx,thLUCAy,thLUCAz],'ZYX')
LLCA_frame.orient(Chassis_frame,'Body',[thLLCAx,thLLCAy,thLLCAz],'ZYX')
LTR_frame.orient(Chassis_frame,'Body',[thLTRx,thLTRy,thLTRz],'XYZ')
LSpdl_frame.orient(Chassis_frame,'Body',[thLSpdlx,thLSpdly,thLSpdlz],'XYZ')
RUCA_frame.orient(Chassis_frame, 'Body', [thRUCAx,thRUCAy,thRUCAz],'ZYX')
RLCA_frame.orient(Chassis_frame,'Body',[thRLCAx,thRLCAy,thRLCAz],'ZYX')
RTR_frame.orient(Chassis_frame,'Body',[thRTRx,thRTRy,thRTRz],'XYZ')
RSpdl_frame.orient(Chassis_frame,'Body',[thRSpdlx,thRSpdly,thRSpdlz],'XYZ')
Hsg_frame.orient(inertial_frame,'Body',[thHsgx,thHsgy,thHsgz],'XYZ')
LBC_frame.orient(Hsg_frame,'Axis',(thLBCy,Hsg_frame.y))
LUB_frame.orient(Chassis_frame,'Body',[thLUBx,thLUBy,thLUBz],'XYZ')
LLB_frame.orient(Chassis_frame,'Body',[thLLBx,thLLBy,thLLBz],'XYZ')
RBC_frame.orient(Hsg_frame,'Axis',(thRBCy,Hsg_frame.y))
RUB_frame.orient(Chassis_frame,'Body',[thRUBx,thRUBy,thRUBz],'XYZ')
RLB_frame.orient(Chassis_frame,'Body',[thRLBx,thRLBy,thRLBz],'XYZ')
Jbar_frame.orient(Chassis_frame,'Body',[thJbarx,thJbary,thJbarz],'XYZ')
LFT_frame.orient(LSpdl_frame,'Axis',(thLFTy,LSpdl_frame.y))
RFT_frame.orient(RSpdl_frame,'Axis',(thRFTy,RSpdl_frame.y))
LRT_frame.orient(Hsg_frame,'Axis',(thLRTy,Hsg_frame.y))
RRT_frame.orient(Hsg_frame,'Axis',(thRRTy,Hsg_frame.y))
LRTeth_frame.orient(Hsg_frame, 'Axis',(thLRTethy, Hsg_frame.y))
RRTeth_frame.orient(Hsg_frame, 'Axis',(thRRTethy, Hsg_frame.y))

# ___________________________________________________________________________________________________________________________
# Point and Location
# Joints

GlobalCoord0 = Point('GlobalCoord0') # Global coordinate system origin location
ChassisC = Point('ChassisC') # Chassis Center, x=0, y=0 on global coordinate system
CGpos = Point('CGpos') # CG position
LUCAMP = Point('LUCAMP') # Control arm midpoints
RUCAMP = Point('RUCAMP')
LLCAMP = Point('LLCAMP')
RLCAMP = Point('RLCAMP')
LUBJ = Point('LUBJ') # Ball joint positions
RUBJ = Point('RUBJ')
LLBJ = Point('LLBJ')
RLBJ = Point('RLBJ')
LFWC = Point('LFWC') # Wheel centers
RFWC = Point('RFWC')
LRWC = Point('LRWC')
RRWC = Point('RRWC')
LFCP = Point('LFCP') # Contact patches
RFCP = Point('RFCP')
LRCP = Point('LRCP')
RRCP = Point('RRCP')
RPC = Point('RPC') # Rack and pinion center
LOTR = Point('LOTR') # OTR points
ROTR = Point('ROTR')
LITR = Point('LITR') # ITR points
RITR = Point('RITR')
HSGC = Point('HSGC') # Housing center
LBCC = Point('LBCC') # Birdcage centers
RBCC = Point('RBCC')
LUBC = Point('LUBC') # Four bar positions at chassis
RUBC = Point('RUBC')
LLBC = Point('LLBC')
RLBC = Point('RLBC')
LUBB = Point('LUBB') # Four bar positions on birdcage
RUBB = Point('RUBB')
LLBB = Point('LLBB')
RLBB = Point('RLBB')
JbarC = Point('JbarC') # Jbar pickup points
JbarH = Point('JbarH')

# Additional Points (Shocks, Springs, Tethers, Etc)

LFShkC = Point('LFShkC') # Shock chassis pivots
RFShkC = Point('RFShkC')
LRShkC = Point('LRShkC')
RRShkC = Point('RRShkC')
FifthShkC = Point('FifthShkC') # Fifth coil shock chassis pivot
TracShkC = Point('TracShkC') # Traction shock chassis pivot
Nine10C = Point('Nine10C') # 9010 shock chassis pivot
LFSpgC = Point('LFSpgC') # Front spring chassis pivots
RFSpgC = Point('RFSpgC')
SixthSpgC = Point('SixthSpgC') # Sixth coil chassis pivot
LFTethC = Point('LFTethC') # Tether chassis pivots
RFTethC = Point('RFTethC')
LRTethC = Point('LRTethC')
RRTethC = Point('RRTethC')

LFShkL = Point('LFShkL') # Shock pivots on lowers
RFShkL = Point('RFShkL')
LRShkB = Point('LRShkB') # Shock pivots on birdcages
RRShkB = Point('RRShkB')
FifthShkH = Point('FifthShkH') # Fifth coil shock pivot on lift bar
TracShkB = Point('TracShkB') # Traction shock pivot on birdcage
Nine10H = Point('Nine10H') # 9010 shock pivot on housing
LFSpgL = Point('LFSpgL') # Spring pivots on lowers
RFSpgL = Point('LFSpgL')
SixthSpgH = Point('SixthSpgH') # Sixth coil pivot on lift bar
LFTethL = Point('LFTethL') # Tether pivots on lowers
RFTethL = Point('RFTethL')
LRTethH = Point('LRTethH') # Tether pivots on housing
RRTethH = Point('RRTethH')

#___________________________________________________________________________________________________________________________________________________
# Define Component Lengths

LUCA_L = symbols('LUCA_L') # Control arm lengths
RUCA_L = symbols('RUCA_L')
LLCA_L = symbols('LLCA_L')
RLCA_L = symbols('RLCA_L')

LUCA_xOff = symbols('LUCA_xOff') # Control arm x-offsets
RUCA_xOff = symbols('RUCA_xOff')
LLCA_xOff = symbols('LLCA_xOff')
RLCA_xOff = symbols('RLCA_xOff')


LTR_L = symbols('LTR_L') # Tierod lengths
RTR_L = symbols('RTR_L')
RP_L = symbols('RP_L') # Rack and pinion length

LUB_L = symbols('LUB_L') # Four bar lengths
RUB_L = symbols('RUB_L')
LLB_L = symbols('LLB_L')
RLB_L = symbols('RLB_L')

Jbar_L = symbols('Jbar_L') # Jbar length

LFSLR = symbols('LFSLR') # Static Loaded Radii
RFSLR = symbols('RFSLR')
LRSLR = symbols('LRSLR')
RRSLR = symbols('RRSLR')

# Additional lengths (Shocks, Springs, Tethers, Etc)

# FINISH ******** FINISH ******** FINISH ******** 
# ******* FINISH ******** FINISH ******** FINISH
# FINISH ******** FINISH ******** FINISH ******** 
# ******* FINISH ******** FINISH ******** FINISH
# FINISH ******** FINISH ******** FINISH *******
# # ******* FINISH ******** FINISH ******** FINISH
# Max Shock Lengths
# Min Shock Lengths
# Spring free lengths
# Spring Coilbind Lengths
# Tether Lengths
# Sixth Coil Length

#___________________________________________________________________________________________________________________________________________________
# Define Position Components

ChassisDeltax = symbols('ChassisDeltax') # Chassis delta amounts from global origin
ChassisDeltay = symbols('ChassisDeltay')
ChassisDeltaz = symbols('ChassisDeltaz')

CGposx = symbols('CGposx') # CG positions
CGposy = symbols('CGposy')
CGposz = symbols('CGposz')

LUCAMPx = symbols('LUCAMPx') # UCA MP position
LUCAMPy = symbols('LUCAMPy')
LUCAMPz = symbols('LUCAMPz')
RUCAMPx = symbols('RUCAMPx')
RUCAMPy = symbols('RUCAMPy')
RUCAMPz = symbols('RUCAMPz')
LLCAMPx = symbols('LLCAMPx') # LCA MP positions
LLCAMPy = symbols('LLCAMPy')
LLCAMPz = symbols('LLCAMPz')
RLCAMPx = symbols('RLCAMPx')
RLCAMPy = symbols('RLCAMPy')
RLCAMPz = symbols('RLCAMPz')

RPCx = symbols('RPCx') # Rack and pinion center postion
RPCy = symbols('RPCy')
RPCz = symbols('RPCz')


LSpdlOff_UBJx = symbols('LSpdlOff_UBJx') # Spindle Offsets
LSpdlOff_UBJy = symbols('LSpdlOff_UBJy')
LSpdlOff_UBJz = symbols('LSpdlOff_UBJz')
RSpdlOff_UBJx = symbols('RSpdlOff_UBJx')
RSpdlOff_UBJy = symbols('RSpdlOff_UBJy')
RSpdlOff_UBJz = symbols('RSpdlOff_UBJz')
LSpdlOff_LBJx = symbols('LSpdlOff_LBJx')
LSpdlOff_LBJy = symbols('LSpdlOff_LBJy')
LSpdlOff_LBJz = symbols('LSpdlOff_LBJz')
RSpdlOff_LBJx = symbols('RSpdlOff_LBJx')
RSpdlOff_LBJy = symbols('RSpdlOff_LBJy')
RSpdlOff_LBJz = symbols('RSpdlOff_LBJz')
LSpdlOff_OTRx = symbols('LSpdlOff_OTRx')
LSpdlOff_OTRy = symbols('LSpdlOff_OTRy')
LSpdlOff_OTRz = symbols('LSpdlOff_OTRz')
RSpdlOff_OTRx = symbols('RSpdlOff_OTRx')
RSpdlOff_OTRy = symbols('RSpdlOff_OTRy')
RSpdlOff_OTRz = symbols('RSpdlOff_OTRz')

HSGCx = symbols('HSGCx') # Housing center position
HSGCy = symbols('HSGCy')
HSGCz = symbols('HSGCz')
LRWCOffy = symbols('LRWCOffy') # Rear Wheel Center Offsets
RRWCOffy = symbols('RRWCOffy')

LBCOffy = symbols('LBCOffy') # Birdcage center offsets
RBCOffy = symbols('RBCOffy')
LBCOff_UBx = symbols('LBCOff_UBx') # Birdcage offsets
LBCOff_UBy = symbols('LBCOff_UBy')
LBCOff_UBz = symbols('LBCOff_UBz')
RBCOff_UBx = symbols('RBCOff_UBx')
RBCOff_UBy = symbols('RBCOff_UBy')
RBCOff_UBz = symbols('RBCOff_UBz')
LBCOff_LBx = symbols('LBCOff_LBx')
LBCOff_LBy = symbols('LBCOff_LBy')
LBCOff_LBz = symbols('LBCOff_LBz')
RBCOff_LBx = symbols('RBCOff_LBx')
RBCOff_LBy = symbols('RBCOff_LBy')
RBCOff_LBz = symbols('RBCOff_LBz')
LBCOff_Shkx = symbols('LBCOff_Shkx')
LBCOff_Shky = symbols('LBCOff_Shky')
LBCOff_Shkz = symbols('LBCOff_Shkz')
RBCOff_Shkx = symbols('RBCOff_Shkx')
RBCOff_Shky = symbols('RBCOff_Shky')
RBCOff_Shkz = symbols('RBCOff_Shkz')
LBCOff_TracShkx = symbols('LBCOff_TracShkx')
LBCOff_TracShky = symbols('LBCOff_TracShky')
LBCOff_TracShkz = symbols('LBCOff_TracShkz')

LUBCx = symbols('LUBCx') # Four bar positions at chassis
LUBCy = symbols('LUBCy')
LUBCz = symbols('LUBCz')
RUBCx = symbols('RUBCx')
RUBCy = symbols('RUBCy')
RUBCz = symbols('RUBCz')
LLBCx = symbols('LLBCx') 
LLBCy = symbols('LLBCy')
LLBCz = symbols('LLBCz')
RLBCx = symbols('RLBCx')
RLBCy = symbols('RLBCy')
RLBCz = symbols('RLBCz')

JbarCx = symbols('JbarCx') # Jbar chassis position
JbarCy = symbols('JbarCy')
JbarCz = symbols('JbarCz')

JbarHOffx = symbols('JbarHOffx') # Jbar housing offsets
JbarHOffy = symbols('JbarHOffy')
JbarHOffz = symbols('JbarHOffz')


LFShkCx = symbols('LFShkCx') # Shock chassis pivot positions
LFShkCy = symbols('LFShkCy')
LFShkCz = symbols('LFShkCz')
RFShkCx = symbols('RFShkCx')
RFShkCy = symbols('RFShkCy')
RFShkCz = symbols('RFShkCz')
LRShkCx = symbols('LRShkCx')
LRShkCy = symbols('LRShkCy')
LRShkCz = symbols('LRShkCz')
RRShkCx = symbols('RRShkCx')
RRShkCy = symbols('RRShkCy')
RRShkCz = symbols('RRShkCz')

TracShkCx = symbols('TracShkCx') # Traction shock chassis positions
TracShkCy = symbols('TracShkCy')
TracShkCz = symbols('TracShkCz')
Nine10ShkCx = symbols('Nine10ShkCx') # 9010 shock chassis positions
Nine10ShkCy = symbols('Nine10ShkCy')
Nine10ShkCz = symbols('Nine10ShkCz')
FifthShkCx = symbols('FifthShkCx') # Fifth coil chassis positions
FifthShkCy = symbols('FifthShkCy')
FifthShkCz = symbols('FifthShkCz')
SixthSpgCx = symbols('SixthSpgCx') # Sixth coil chassis positions
SixthSpgCy = symbols('SixthSpgCy')
SixthSpgCz = symbols('SixthSpgCz')

LFShkLx = symbols('LFShkLx') # Shock lower pivot positions
LFShkLy = symbols('LFShkLy')
LFShkLz = symbols('LFShkLz')
RFShkLx = symbols('RFShkLx')
RFShkLy = symbols('RFShkLy')
RFShkLz = symbols('RFShkLz')
LRShkBx = symbols('LRShkBx') # Shock birdcage pivot positions
LRShkBy = symbols('LRShkBy')
LRShkBz = symbols('LRShkBz')
RRShkBx = symbols('RRShkBx')
RRShkBy = symbols('RRShkBy')
RRShkBz = symbols('RRShkBz')
TracShkBx = symbols('TracShkBx') # Traction shock birdcage positions
TracShkBy = symbols('TracShkBy')
TracShkBz = symbols('TracShkBz')
FifthShkHOffx = symbols('FifthShkHOffx') # Fifth coil housing offsets
FifthShkHOffy = symbols('FifthShkHOffy')
FifthShkHOffz = symbols('FifthShkHOffz')
Nine10ShkHOffx = symbols('Nine10ShkHOffx') # 9010 shock housing offsets
Nine10ShkHOffy = symbols('Nine10ShkHOffy')
Nine10ShkHOffz = symbols('Nine10ShkHOffz')
SixthSpgHOffx = symbols('SixthSpgHOffx') # Sixth coil housing offsets
SixthSpgHOffy = symbols('SixthSpgHOffy')
SixthSpgHOffz = symbols('SixthSpgHOffz')

LFSpgCx = symbols('LFSpgCx') # Front spring chassis positions
LFSpgCy = symbols('LFSpgCy')
LFSpgCz = symbols('LFSpgCz')
RFSpgCx = symbols('RFSpgCx')
RFSpgCy = symbols('RFSpgCy')
RFSpgCz = symbols('RFSpgCz')

LFSpgLx = symbols('LFSpgLx') # Front spring lower positions
LFSpgLy = symbols('LFSpgLy')
LFSpgLz = symbols('LFSpgLz')
RFSpgLx = symbols('RFSpgLx')
RFSpgLy = symbols('RFSpgLy')
RFSpgLz = symbols('RFSpgLz')

LFTethCx = symbols('LFTethCx') # Tether chassis positions
LFTethCy = symbols('LFTethCy') 
LFTethCz = symbols('LFTethCz')
RFTethCx = symbols('RFTethCx')
RFTethCy = symbols('RFTethCy')
RFTethCz = symbols('RFTethCz')
LRTethCx = symbols('LRTethCx')
LRTethCy = symbols('LRTethCy')
LRTethCz = symbols('LRTethCz')
RRTethCx = symbols('RRTethCx')
RRTethCy = symbols('RRTethCy')
RRTethCz = symbols('RRTethCz')

LFTethLx = symbols('LFTethLx') # Tether lower positions
LFTethLy = symbols('LFTethLy') 
LFTethLz = symbols('LFTethLz')
RFTethLx = symbols('RFTethLx')
RFTethLy = symbols('RFTethLy')
RFTethLz = symbols('RFTethLz') 
LRTethHy = symbols('LRTethHy') # Tether housing positions
RRTethHy = symbols('RRTethHy')

#___________________________________________________________________________________________________________________________________________________
# Set Chassis Positions

ChassisC.set_pos(GlobalCoord0,(ChassisDeltax * inertial_frame.x + ChassisDeltay * inertial_frame.y + ChassisDeltaz * inertial_frame.z)) # Chassis 
CGpos.set_pos(ChassisC,(CGposx * Chassis_frame.x + CGposy * Chassis_frame.y + CGposz * Chassis_frame.z)) # CG Position
LUCAMP.set_pos(ChassisC,(LUCAMPx * Chassis_frame.x + LUCAMPy * Chassis_frame.y + LUCAMPz * Chassis_frame.z)) # Control Arm Mount Midpoints
RUCAMP.set_pos(ChassisC,(RUCAMPx * Chassis_frame.x + RUCAMPy * Chassis_frame.y + RUCAMPz * Chassis_frame.z))
LLCAMP.set_pos(ChassisC,(LLCAMPx * Chassis_frame.x + LLCAMPy * Chassis_frame.y + LLCAMPz * Chassis_frame.z))
RLCAMP.set_pos(ChassisC,(RLCAMPx * Chassis_frame.x + RLCAMPy * Chassis_frame.y + RLCAMPz * Chassis_frame.z))
LUBC.set_pos(ChassisC,(LUBCx * Chassis_frame.x + LUBCy * Chassis_frame.y + LUBCz * Chassis_frame.z)) # Four bar chassis positions
RUBC.set_pos(ChassisC,(RUBCx * Chassis_frame.x + RUBCy * Chassis_frame.y + RUBCz * Chassis_frame.z))
LLBC.set_pos(ChassisC,(LLBCx * Chassis_frame.x + LLBCy * Chassis_frame.y + LLBCz * Chassis_frame.z))
RLBC.set_pos(ChassisC,(RLBCx * Chassis_frame.x + RLBCy * Chassis_frame.y + RLBCz * Chassis_frame.z))
FifthShkC.set_pos(ChassisC,(FifthShkCx * Chassis_frame.x + FifthShkCy * Chassis_frame.y + FifthShkCz * Chassis_frame.z)) # Fifth coil chassis position
JbarC.set_pos(ChassisC,(JbarCx * Chassis_frame.x + JbarCy * Chassis_frame.y + JbarCz * Chassis_frame.z)) # Jbar chassis position
LFShkC.set_pos(ChassisC,(LFShkCx * Chassis_frame.x + LFShkCy * Chassis_frame.y + LFShkCz * Chassis_frame.z)) # Shock chassis positions
RFShkC.set_pos(ChassisC,(RFShkCx * Chassis_frame.x + RFShkCy * Chassis_frame.y + RFShkCz * Chassis_frame.z))
LRShkC.set_pos(ChassisC,(LRShkCx * Chassis_frame.x + LRShkCy * Chassis_frame.y + LRShkCz * Chassis_frame.z))
RRShkC.set_pos(ChassisC,(RRShkCx * Chassis_frame.x + RRShkCy * Chassis_frame.y + RRShkCz * Chassis_frame.z))
TracShkC.set_pos(ChassisC,(TracShkCx * Chassis_frame.x + TracShkCy * Chassis_frame.y + TracShkCz * Chassis_frame.z)) 
Nine10C.set_pos(ChassisC,(Nine10ShkCx * Chassis_frame.x + Nine10ShkCy * Chassis_frame.y + Nine10ShkCz * Chassis_frame.z))
LFSpgC.set_pos(ChassisC,(LFSpgCx * Chassis_frame.x + LFSpgCy * Chassis_frame.y + LFSpgCz * Chassis_frame.z)) # Spring chassis positions
RFSpgC.set_pos(ChassisC,(RFSpgCx * Chassis_frame.x + RFSpgCy * Chassis_frame.y + RFSpgCz * Chassis_frame.z))
SixthSpgC.set_pos(ChassisC,(SixthSpgCx * Chassis_frame.x + SixthSpgCy * Chassis_frame.y + SixthSpgCz * Chassis_frame.z))
LFTethC.set_pos(ChassisC,(LFTethCx * Chassis_frame.x + LFTethCy * Chassis_frame.y + LFTethCz * Chassis_frame.z)) # Tether chassis positions
RFTethC.set_pos(ChassisC,(RFTethCx * Chassis_frame.x + RFTethCy * Chassis_frame.y + RFTethCz * Chassis_frame.z))
LRTethC.set_pos(ChassisC,(LRTethCx * Chassis_frame.x + LRTethCy * Chassis_frame.y + LRTethCz * Chassis_frame.z))
RRTethC.set_pos(ChassisC,(RRTethCx * Chassis_frame.x + RRTethCy * Chassis_frame.y + RRTethCz * Chassis_frame.z))

LUBJ.set_pos(LUCAMP,(LUCA_xOff * LUCA_frame.x - LUCA_L * LUCA_frame.y + 0 * LUCA_frame.z)) # Balljoint positions
RUBJ.set_pos(RUCAMP,(RUCA_xOff * RUCA_frame.x + RUCA_L * RUCA_frame.y + 0 * RUCA_frame.z))
LLBJ.set_pos(LLCAMP,(LLCA_xOff * LLCA_frame.x - LLCA_L * LLCA_frame.y + 0 * LLCA_frame.z))
RLBJ.set_pos(RLCAMP,(RLCA_xOff * RLCA_frame.x + RLCA_L * RLCA_frame.y + 0 * RLCA_frame.z))
LFShkL.set_pos(LLCAMP,(LFShkLx * LLCA_frame.x - LFShkLy * LLCA_frame.y + LFShkCz * LLCA_frame.z)) # Shock positions on LCA
RFShkL.set_pos(RLCAMP,(RFShkLx * RLCA_frame.x + RFShkLy * RLCA_frame.y + RFShkCz * RLCA_frame.z))
LFSpgL.set_pos(LLCAMP,(LFSpgLx * LLCA_frame.x - LFSpgLy * LLCA_frame.y + LFShkCz * LLCA_frame.z)) # Shock positions on birdcages
RFSpgL.set_pos(RLCAMP,(RFSpgLx * RLCA_frame.x + RFSpgLy * RLCA_frame.y + RFShkCz * RLCA_frame.z))
LFTethL.set_pos(LLCAMP,(LFTethCx * LLCA_frame.x - LFTethCy * LLCA_frame.y + LFTethCz * LLCA_frame.z)) # Tether positions on LCA
RFTethL.set_pos(RLCAMP,(RFTethCx * RLCA_frame.x + RFTethCy * RLCA_frame.y + RFTethCz * RLCA_frame.z))

RPC.set_pos(ChassisC,(RPCx * Chassis_frame.x + RPCy * Chassis_frame.y + RPCz * Chassis_frame.z)) # Rack and pinion center position
LITR.set_pos(RPC,(0 * RP_frame.x + (-RP_L / 2) * RP_frame.y + 0 * RP_frame.z)) # ITR positions
RITR.set_pos(RPC,(0 * RP_frame.x + (RP_L / 2) * RP_frame.y + 0 * RP_frame.z))

HSGC.set_pos(GlobalCoord0,(HSGCx * inertial_frame.x + HSGCy * inertial_frame.y + HSGCz * inertial_frame.z)) # Housing center position
LBCC.set_pos(HSGC,(0 * Hsg_frame.x + LBCOffy * Hsg_frame.y + 0 * Hsg_frame.z)) # Birdcage center positions
RBCC.set_pos(HSGC,(0 * Hsg_frame.x + RBCOffy * Hsg_frame.y + 0 * Hsg_frame.z))
LRTethH.set_pos(HSGC,(0 * Hsg_frame.x + LRTethHy * Hsg_frame.y + 0 * Hsg_frame.z)) # Tether housing positions
RRTethH.set_pos(HSGC,(0 * Hsg_frame.x + RRTethHy * Hsg_frame.y + 0 * Hsg_frame.z))
LUBB.set_pos(LBCC,(LBCOff_UBx * LBC_frame.x + LBCOff_UBy * LBC_frame.y + LBCOff_UBz * LBC_frame.z)) # Four bar birdcage positions
RUBB.set_pos(RBCC,(RBCOff_UBx * RBC_frame.x + RBCOff_UBy * RBC_frame.y + RBCOff_UBz * RBC_frame.z))
LLBB.set_pos(LBCC,(LBCOff_LBx * LBC_frame.x + LBCOff_LBy * LBC_frame.y + LBCOff_LBz * LBC_frame.z))
RLBB.set_pos(RBCC,(RBCOff_LBx * RBC_frame.x + RBCOff_LBy * RBC_frame.y + RBCOff_LBz * RBC_frame.z))
LRShkB.set_pos(LBCC,(LBCOff_Shkx * LBC_frame.x + LBCOff_Shky * LBC_frame.y + LBCOff_Shkz * LBC_frame.z)) # Shock birdcage positions
RRShkB.set_pos(RBCC,(RBCOff_Shkx * RBC_frame.x + RBCOff_Shky * RBC_frame.y + RBCOff_Shkz * RBC_frame.z))
TracShkB.set_pos(TracShkB,(TracShkBx * LBC_frame.x + TracShkBy * LBC_frame.y + TracShkBz * LBC_frame.z))
FifthShkH.set_pos(HSGC,(FifthShkHOffx * Hsg_frame.x + FifthShkHOffy * Hsg_frame.y + FifthShkHOffz * Hsg_frame.z)) # Fifth coil housing position
Nine10H.set_pos(HSGC,(Nine10ShkHOffx * Hsg_frame.x + Nine10ShkHOffy * Hsg_frame.y + Nine10ShkHOffz * Hsg_frame.z)) # 9010 housing position
SixthSpgH.set_pos(HSGC,(SixthSpgHOffx * Hsg_frame.x + SixthSpgHOffy * Hsg_frame.y + SixthSpgHOffz * Hsg_frame.z)) # Sixth coil housing position

LFCP.set_pos(LFWC,(0 * LFT_frame.x + 0 * LFT_frame.y - LFSLR * LFT_frame.z)) # Contact patch positions
RFCP.set_pos(RFWC,(0 * RFT_frame.x + 0 * RFT_frame.y - RFSLR * RFT_frame.z))
LRCP.set_pos(LRWC,(0 * LRT_frame.x + 0 * LRT_frame.y - LRSLR * LRT_frame.z))
RRCP.set_pos(RRWC,(0 * RRT_frame.x + 0 * RRT_frame.y - RRSLR * RRT_frame.z))

LFWC.set_pos(LUBJ,(LSpdlOff_LBJx * LSpdl_frame.x + LSpdlOff_LBJy * LSpdl_frame.y + LSpdlOff_LBJz * LSpdl_frame.z)) # Wheel center positions
RFWC.set_pos(RUBJ,(RSpdlOff_LBJx * RSpdl_frame.x + RSpdlOff_LBJy * RSpdl_frame.y + RSpdlOff_LBJz * RSpdl_frame.z))
LRWC.set_pos(HSGC,(0 * Hsg_frame.x + LRWCOffy * Hsg_frame.y + 0 * Hsg_frame.z))
RRWC.set_pos(HSGC,(0 * Hsg_frame.x + RRWCOffy * Hsg_frame.y + 0 * Hsg_frame.z))

LOTR.set_pos(LFWC,(LSpdlOff_OTRx * LSpdl_frame.x + LSpdlOff_OTRy * LSpdl_frame.y + LSpdlOff_OTRz * LSpdl_frame.z)) # OTR positions
ROTR.set_pos(RFWC,(RSpdlOff_OTRx * RSpdl_frame.x + RSpdlOff_OTRy * RSpdl_frame.y + RSpdlOff_OTRz * RSpdl_frame.z))

#____________________________________________________________________________________________________________________________
# Center of Mass Locations

# Exercise
# The mass centers of the three bodies can be located in a similar fashion.
# The distances  dL,dU,dTdL,dU,dT  locate the mass centers relative to the distal end of the body segments.

CoM_Chassis = Point('CoM_Chassis')
CoM_Chassis.set_pos(CGpos,0)
CoM_RP = Point('CoM_RP')
CoM_RP.set_pos(RPC,0)
CoM_LUCA = Point('CoM_LUCA')
CoM_LUCA.set_pos(LUCAMP, ((LUCA_xOff / 2) * LUCA_frame.x + (-LUCA_L / 2) * LUCA_frame.y + 0 * LUCA_frame.z))
CoM_RUCA = Point('CoM_RUCA')
CoM_RUCA.set_pos(RUCAMP, ((RUCA_xOff / 2) * RUCA_frame.x + (RUCA_L / 2) * RUCA_frame.y + 0 * RUCA_frame.z))
CoM_LLCA = Point('CoM_LLCA')
CoM_LLCA.set_pos(LLCAMP, ((LLCA_xOff / 2) * LLCA_frame.x + (-LLCA_L / 2) * LLCA_frame.y + 0 * LLCA_frame.z))
CoM_RLCA = Point('CoM_RLCA')
CoM_RLCA.set_pos(RLCAMP, ((RLCA_xOff / 2) * RLCA_frame.x + (RLCA_L / 2) * RLCA_frame.y + 0 * RLCA_frame.z))
CoM_LSpdl = Point('CoM_LSpdl')
CoM_LSpdl.set_pos(LFWC,(0 * LSpdl_frame.x + 0 * LSpdl_frame.y + 0 * LSpdl_frame.z))
CoM_RSpdl = Point('CoM_RSpdl')
CoM_RSpdl.set_pos(LFWC,(0 * RSpdl_frame.x + 0 * RSpdl_frame.y + 0 * RSpdl_frame.z))
CoM_LTR = Point('CoM_LTR')
CoM_LTR.set_pos(LITR, ((LTR_L / 2) * LTR_frame.x + (-LTR_L / 2) * LTR_frame.y + (LTR_L / 2) * LTR_frame.z))
CoM_RTR = Point('CoM_RTR')
CoM_RTR.set_pos(RITR, ((RTR_L / 2) * RTR_frame.x + (RTR_L / 2) * RTR_frame.y + (RTR_L / 2) * RTR_frame.z))
CoM_Hsg = Point('CoM_Hsg')
CoM_Hsg.set_pos(HSGC, (0 * Hsg_frame.x + 0 * Hsg_frame.y + 0 * Hsg_frame.z))
CoM_LBC = Point('CoM_LBC')
CoM_LBC.set_pos(LBCC, (0 * LBC_frame.x + 0 * LBC_frame.y + 0 * LBC_frame.z))
CoM_RBC = Point('CoM_RBC')
CoM_RBC.set_pos(RBCC, (0 * RBC_frame.x + 0 * RBC_frame.y + 0 * RBC_frame.z))
CoM_LUB = Point('CoM_LUB')
CoM_LUB.set_pos(LUBC, ((LUB_L / 2) * LUB_frame.x + 0 * LUB_frame.y + 0 * LUB_frame.z))
CoM_RUB = Point('CoM_RUB')
CoM_RUB.set_pos(RUBC, ((RUB_L / 2) * RUB_frame.x + 0 * RUB_frame.y + 0 * RUB_frame.z))
CoM_LLB = Point('CoM_LLB')
CoM_LLB.set_pos(LLBC, ((LLB_L / 2) * LLB_frame.x + 0 * LLB_frame.y + 0 * LLB_frame.z))
CoM_RLB = Point('CoM_RLB')
CoM_RLB.set_pos(RLBC, ((RLB_L / 2) * RLB_frame.x + 0 * RLB_frame.y + 0 * RLB_frame.z))
CoM_Jbar = Point('CoM_Jbar')
CoM_Jbar.set_pos(JbarC,((Jbar_L / 2) * Jbar_frame.x + 0 * Jbar_frame.y + 0 * Jbar_frame.z))
CoM_LFT = Point('CoM_LFT')
CoM_LFT.set_pos(LFWC, (0 * LFT_frame.x + 0 * LFT_frame.y + 0 * LFT_frame.z))
CoM_RFT = Point('CoM_RFT')
CoM_RFT.set_pos(RFWC, (0 * RFT_frame.x + 0 * RFT_frame.y + 0 * RFT_frame.z))
CoM_LRT = Point('CoM_LRT')
CoM_LRT.set_pos(LRWC, (0 * LRT_frame.x + 0 * LRT_frame.y + 0 * LRT_frame.z))
CoM_RRT = Point('CoM_RRT')
CoM_RRT.set_pos(RRWC, (0 * RRT_frame.x + 0 * RRT_frame.y + 0 * RRT_frame.z))

# _________________________________________________________________________________________________________________________
# Kinematic Differential Equations

# At this point, we are going to select three generalized speeds,  ω1ω1 ,  ω2ω2 , and  ω3ω3 , (the angular velocities of the joints) 
# so that the time derivative of the generalized coordinates are equal to the genearlized speeds. These relationships are called the
# kinematical differential equations and allow for the remaining equations of motion to easily be derived in first order form.
# This step is explicit when using Kane's method, which we are going to use. First create the time varying symbols:

# Generalized Speeds

wRoll, wPitch, wYaw = dynamicsymbols('wRoll, wPitch, wYaw')
wLUCAx, wLLCAx, wRUCAx, wRLCAx = dynamicsymbols('wLUCAx, wLLCAx, wRUCAx, wRLCAx')
wLTRx,wLTRy,wLTRz = dynamicsymbols('wLTRx,wLTRy,wLTRz')
wLSpdlx,wLSpdly,wLSpdlz = dynamicsymbols('wLSpdlx,wLSpdly,wLSpdlz')
wRTRx,wRTRy,wRTRz = dynamicsymbols('wRTRx,wRTRy,wRTRz')
wRSpdlx,wRSpdly,wRSpdlz = dynamicsymbols('wRSpdlx,wRSpdly,wRSpdlz')
wHsgx, wHsgy, wHsgz = dynamicsymbols('wHsgx, wHsgy, wHsgz')
wLBCy, wRBCy = dynamicsymbols('wLBCy, wRBCy')
wLUBx, wLUBy, wLUBz = dynamicsymbols('wLUBx, wLUBy, wLUBz')
wRUBx, wRUBy, wRUBz = dynamicsymbols('wRUBx, wRUBy, wRUBz')
wLLBx, wLLBy, wLLBz = dynamicsymbols('wLLBx, wLLBy, wLLBz')
wRLBx, wRLBy, wRLBz = dynamicsymbols('wRLBx, wRLBy, wRLBz')
wJbarx, wJbary, wJbarz = dynamicsymbols('wJbarx, wJbary, wJbarz')
wLFTy, wRFTy, wLRTy, wRRTy = dynamicsymbols('wLFTy, wRFTy, wLRTy, wRRTy')
veltransRPy = dynamicsymbols('veltransRPy') # Dynamic symbol for the translation of we rack and pinion

# To enforce the relationships:  ωn=θ˙nωn=θ˙n  we define these three equations  ωn−θ˙n=0ωn−θ˙n=0 :
# Kinematic Differential Equations

kinematical_differential_equations = [wRoll - thRoll.diff(),wPitch - thPitch.diff(),wYaw - thYaw.diff(),
                                      wLUCAx - thLUCAx.diff(),wLLCAx - thLLCAx.diff(),wRUCAx - thRUCAx.diff(),wRLCAx - thRLCAx.diff(),
                                      wLTRx - thLTRx.diff(),wLTRy - thLTRy.diff(),wLTRz - thLTRz.diff(),
                                      wRTRx - thRTRx.diff(),wRTRy - thRTRy.diff(),wRTRz - thRTRz.diff(),
                                      wLSpdlx - thLSpdlx.diff(),wLSpdly - thLSpdly.diff(),wLSpdlz - thLSpdlz.diff(),
                                      wRSpdlx - thRSpdlx.diff(),wRSpdly - thRSpdly.diff(),wRSpdlz - thRSpdlz.diff(),
                                      wHsgx - thHsgx.diff(),wHsgy - thHsgy.diff(),wHsgz - thHsgz.diff(),
                                      wLBCy - thLBCy.diff(),wRBCy - thRBCy.diff(),
                                      wLUBx - thLUBx.diff(),wLUBy - thLUBy.diff(),wLUBz - thLUBz.diff(),
                                      wRUBx - thRUBx.diff(),wRUBy - thRUBy.diff(),wRUBz - thRUBz.diff(),
                                      wLLBx - thLLBx.diff(),wLLBy - thLLBy.diff(),wLLBz - thLLBz.diff(),
                                      wRLBx - thRLBx.diff(),wRLBy - thRLBy.diff(),wRLBz - thRLBz.diff(),
                                      wJbarx - thJbarx.diff(),wJbary - thJbary.diff(),wJbarz - thJbarz.diff(),
                                      wLFTy - thLFTy.diff(),wRFTy - thRFTy.diff(),wLRTy - thLRTy.diff(),wRRTy - thRRTy.diff(),
                                      veltransRPy - transRPy.diff()]


# ______________________________________________________________________________________________________________________________
# Angular Velocities
# Now we can use the generalized speeds to define the angular velocities of the reference frames. Due to our definitions of rotations these are simply  ωnk̂ ωnk^ .
# Hint: Remember how we located the joint centers and center of mass locations. The syntax is very similar here.

#lower_leg_frame.set_ang_vel(inertial_frame,omega1*inertial_frame.z) # Sets the angular velocity relative to a reference frame
#lower_leg_frame.ang_vel_in(inertial_frame) # Describe the frame's angular velocity in terms of another reference frame

Chassis_frame.set_ang_vel(inertial_frame,(wRoll * Chassis_frame.x + wPitch * Chassis_frame.y + wYaw * Chassis_frame.z))
#RP_frame.set_ang_vel(Chassis_frame,[wRPx,wRPy,wRPz])#Not needed because RP does not have an angular velocity
LUCA_frame.set_ang_vel(Chassis_frame,(wLUCAx * LUCA_frame.x))
RUCA_frame.set_ang_vel(Chassis_frame,(wRUCAx * RUCA_frame.x))
LLCA_frame.set_ang_vel(Chassis_frame,(wLLCAx * LLCA_frame.x))
RLCA_frame.set_ang_vel(Chassis_frame,(wLUCAx * RLCA_frame.x))
LSpdl_frame.set_ang_vel(Chassis_frame,(wLSpdlx * LSpdl_frame.x + wLSpdly * LSpdl_frame.y + wLSpdlz * LSpdl_frame.z))
RSpdl_frame.set_ang_vel(Chassis_frame,(wRSpdlx * RSpdl_frame.x + wRSpdly * RSpdl_frame.y + wRSpdlz * RSpdl_frame.z))
LTR_frame.set_ang_vel(Chassis_frame,(wLTRx * LTR_frame.x + wLTRy * LTR_frame.y + wLTRz * LTR_frame.z))
RTR_frame.set_ang_vel(Chassis_frame,(wRTRx * RTR_frame.x + wRTRy * RTR_frame.y + wRTRz * RTR_frame.z))
Hsg_frame.set_ang_vel(inertial_frame,(wHsgx * Hsg_frame.x + wHsgy * Hsg_frame.y + wHsgz * Hsg_frame.z))
LBC_frame.set_ang_vel(Hsg_frame,(wLBCy * LBC_frame.y))
RBC_frame.set_ang_vel(Hsg_frame,(wRBCy * RBC_frame.y))
LUB_frame.set_ang_vel(Chassis_frame,(wLUBx * LUB_frame.x + wLUBy * LUB_frame.y + wLUBz * LUB_frame.z))
RUB_frame.set_ang_vel(Chassis_frame,(wRUBx * RUB_frame.x + wRUBy * RUB_frame.y + wRUBz * RUB_frame.z))
LLB_frame.set_ang_vel(Chassis_frame,(wLLBx * LLB_frame.x + wLLBy * LLB_frame.y + wLLBz * LLB_frame.z))
RLB_frame.set_ang_vel(Chassis_frame,(wRLBx * RLB_frame.x + wRLBy * RLB_frame.y + wRLBz * RLB_frame.z))
Jbar_frame.set_ang_vel(Chassis_frame,(wJbarx * Jbar_frame.x + wJbary * Jbar_frame.y + wJbarz * Jbar_frame.z))
LFT_frame.set_ang_vel(LSpdl_frame,(wLFTy * LFT_frame.y))
RFT_frame.set_ang_vel(RSpdl_frame,(wRFTy * RFT_frame.y))
LRT_frame.set_ang_vel(Hsg_frame,(wLRTy * LRT_frame.y))
RRT_frame.set_ang_vel(Hsg_frame,(wRRTy * RRT_frame.y))
#LRTeth_frame.set_ang_vel(Hsg_frame, 'Axis',(wLRTewy, Hsg_frame.y))
#RRTeth_frame.set_ang_vel(Hsg_frame, 'Axis',(wRRTewy, Hsg_frame.y))

# ______________________________________________________________________________________________________________________________
# Linear Velocities
# Finally, the linear velocities of the mass centers are needed. 

GlobalCoord0.set_vel(inertial_frame,0)
CoM_RP.set_vel(RP_frame,veltransRPy * RP_frame.y)
CoM_Chassis.v2pt_theory(GlobalCoord0,inertial_frame,Chassis_frame)
CoM_LUCA.v2pt_theory(GlobalCoord0,inertial_frame,LUCA_frame)
CoM_RUCA.v2pt_theory(GlobalCoord0,inertial_frame,RUCA_frame)
CoM_LLCA.v2pt_theory(GlobalCoord0,inertial_frame,LLCA_frame)
CoM_RLCA.v2pt_theory(GlobalCoord0,inertial_frame,RUCA_frame)
CoM_LSpdl.v2pt_theory(GlobalCoord0,inertial_frame,LSpdl_frame)
CoM_RSpdl.v2pt_theory(GlobalCoord0,inertial_frame,RSpdl_frame)
CoM_LTR.v2pt_theory(GlobalCoord0,inertial_frame,LTR_frame)
CoM_RTR.v2pt_theory(GlobalCoord0,inertial_frame,RTR_frame)
CoM_Hsg.v2pt_theory(GlobalCoord0,inertial_frame,Hsg_frame)
CoM_LBC.v2pt_theory(GlobalCoord0,inertial_frame,LBC_frame)
CoM_RBC.v2pt_theory(GlobalCoord0,inertial_frame,RBC_frame)
CoM_LUB.v2pt_theory(GlobalCoord0,inertial_frame,LUB_frame)
CoM_RUB.v2pt_theory(GlobalCoord0,inertial_frame,RUB_frame)
CoM_LLB.v2pt_theory(GlobalCoord0,inertial_frame,LLB_frame)
CoM_RLB.v2pt_theory(GlobalCoord0,inertial_frame,RLB_frame)
CoM_Jbar.v2pt_theory(GlobalCoord0,inertial_frame,Jbar_frame)
CoM_LFT.v2pt_theory(GlobalCoord0,inertial_frame,LSpdl_frame)
CoM_RFT.v2pt_theory(GlobalCoord0,inertial_frame,RSpdl_frame)
CoM_LRT.v2pt_theory(GlobalCoord0,inertial_frame,Hsg_frame)
CoM_RRT.v2pt_theory(GlobalCoord0,inertial_frame,Hsg_frame)

# ______________________________________________________________________________________________________________________________
# Define inertias

from sympy.physics.mechanics import inertia, RigidBody
from sympy import symbols

# Mass
# The masses of each rigid body can be represented by constant values, so we create a symbol for each body.

#lower_leg_mass, upper_leg_mass, torso_mass = symbols('m_L, m_U, m_T')
m_Chassis, m_LUCA, m_RUCA, m_LLCA, m_RLCA = symbols('m_Chassis, m_LUCA, m_RUCA, m_LLCA, m_RLCA')
m_LSpdl, m_RSpdl, m_LTR, m_RTR, m_RP, m_Hsg = symbols('m_LSpdl, m_RSpdl, m_LTR, m_RTR, m_RP, m_Hsg')
m_LBC, m_RBC, m_LUB, m_RUB, m_LLB, m_RLB, m_Jbar = symbols('m_LBC, m_RBC, m_LUB, m_RUB, m_LLB, m_RLB, m_Jbar')
m_LFT, m_RFT, m_LRT, m_RRT = symbols('m_LFT, m_RFT, m_LRT, m_RRT')

# Inertia

Chassis_Ixx, Chassis_Iyy, Chassis_Izz = symbols('Chassis_Ixx, Chassis_Iyy, Chassis_Izz')
Chassis_Ixy, Chassis_Iyz, Chassis_Izx = symbols('Chassis_Ixy, Chassis_Iyz, Chassis_Izx')
RP_Ixx, RP_Iyy, RP_Izz = symbols('RP_Ixx, RP_Iyy, RP_Izz')
LUCA_Ixx, LUCA_Iyy, LUCA_Izz = symbols('LUCA_Ixx, LUCA_Iyy, LUCA_Izz')
RUCA_Ixx, RUCA_Iyy, RUCA_Izz = symbols('RUCA_Ixx, RUCA_Iyy, RUCA_Izz')
LLCA_Ixx, LLCA_Iyy, LLCA_Izz = symbols('LLCA_Ixx, LLCA_Iyy, LLCA_Izz')
RLCA_Ixx, RLCA_Iyy, RLCA_Izz = symbols('RLCA_Ixx, RLCA_Iyy, RLCA_Izz')
LSpdl_Ixx, LSpdl_Iyy, LSpdl_Izz = symbols('LSpdl_Ixx, LSpdl_Iyy, LSpdl_Izz')
RSpdl_Ixx, RSpdl_Iyy, RSpdl_Izz = symbols('RSpdl_Ixx, RSpdl_Iyy, RSpdl_Izz')
LTR_Ixx, LTR_Iyy, LTR_Izz = symbols('LTR_Ixx, LTR_Iyy, LTR_Izz')
RTR_Ixx, RTR_Iyy, RTR_Izz = symbols('RTR_Ixx, RTR_Iyy, RTR_Izz')
Hsg_Ixx, Hsg_Iyy, Hsg_Izz = symbols('Hsg_Ixx, Hsg_Iyy, Hsg_Izz')
LBC_Ixx, LBC_Iyy, LBC_Izz = symbols('LBC_Ixx, LBC_Iyy, LBC_Izz')
RBC_Ixx, RBC_Iyy, RBC_Izz = symbols('RBC_Ixx, RBC_Iyy, RBC_Izz')
LUB_Ixx, LUB_Iyy, LUB_Izz = symbols('LUB_Ixx, LUB_Iyy, LUB_Izz')
RUB_Ixx, RUB_Iyy, RUB_Izz = symbols('RUB_Ixx, RUB_Iyy, RUB_Izz')
LLB_Ixx, LLB_Iyy, LLB_Izz = symbols('LLB_Ixx, LLB_Iyy, LLB_Izz')
RLB_Ixx, RLB_Iyy, RLB_Izz = symbols('RLB_Ixx, RLB_Iyy, RLB_Izz')
Jbar_Ixx, Jbar_Iyy, Jbar_Izz = symbols('Jbar_Ixx, Jbar_Iyy, Jbar_Izz')
LFT_Ixx, LFT_Iyy, LFT_Izz = symbols('LFT_Ixx, LFT_Iyy, LFT_Izz')
RFT_Ixx, RFT_Iyy, RFT_Izz = symbols('RFT_Ixx, RFT_Iyy, RFT_Izz')
LRT_Ixx, LRT_Iyy, LRT_Izz = symbols('LRT_Ixx, LRT_Iyy, LRT_Izz')
RRT_Ixx, RRT_Iyy, RRT_Izz = symbols('RRT_Ixx, RRT_Iyy, RRT_Izz')

# The inertia() function is a convenience function for creating inertia dyadics (i.e. basis dependent tensors). 
# You specify a reference frame to define the inertia with respect to and at a minimum for symmetric bodies
# provide the diagonal entries of the inertia tensor. 

Chassis_dyadic = inertia(Chassis_frame,Chassis_Ixx,Chassis_Iyy,Chassis_Izz,Chassis_Ixy,Chassis_Iyz,Chassis_Izx)
RP_dyadic = inertia(RP_frame,RP_Ixx,RP_Iyy,RP_Izz)
LUCA_dyadic = inertia(LUCA_frame,LUCA_Ixx,LUCA_Iyy,LUCA_Izz)
RUCA_dyadic = inertia(RUCA_frame,RUCA_Ixx,RUCA_Iyy,RUCA_Izz)
LLCA_dyadic = inertia(LLCA_frame,LLCA_Ixx,LLCA_Iyy,LLCA_Izz)
RLCA_dyadic = inertia(RLCA_frame,RLCA_Ixx,RLCA_Iyy,RLCA_Izz)
LSpdl_dyadic = inertia(LSpdl_frame,LSpdl_Ixx,LSpdl_Iyy,LSpdl_Izz)
RSpdl_dyadic = inertia(RSpdl_frame,RSpdl_Ixx,RSpdl_Iyy,RSpdl_Izz)
LTR_dyadic = inertia(LTR_frame,LTR_Ixx,LTR_Iyy,LTR_Izz)
RTR_dyadic = inertia(RTR_frame,RTR_Ixx,RTR_Iyy,RTR_Izz)
Hsg_dyadic = inertia(Hsg_frame,Hsg_Ixx,Hsg_Iyy,Hsg_Izz)
LBC_dyadic = inertia(LBC_frame,LBC_Ixx,LBC_Iyy,LBC_Izz)
RBC_dyadic = inertia(RBC_frame,RBC_Ixx,RBC_Iyy,RBC_Izz)
LUB_dyadic = inertia(LUB_frame,LUB_Ixx,LUB_Iyy,LUB_Izz)
RUB_dyadic = inertia(RUB_frame,RUB_Ixx,RUB_Iyy,RUB_Izz)
LLB_dyadic = inertia(LLB_frame,LLB_Ixx,LLB_Iyy,LLB_Izz)
RLB_dyadic = inertia(RLB_frame,RLB_Ixx,RLB_Iyy,RLB_Izz)
Jbar_dyadic = inertia(Jbar_frame,Jbar_Ixx,Jbar_Iyy,Jbar_Izz)
LFT_dyadic = inertia(LFT_frame,LFT_Ixx,LFT_Iyy,LFT_Izz)
RFT_dyadic = inertia(RFT_frame,RFT_Ixx,RFT_Iyy,RFT_Izz)
LRT_dyadic = inertia(LRT_frame,LRT_Ixx,LRT_Iyy,LRT_Izz)
RRT_dyadic = inertia(RRT_frame,RRT_Ixx,RRT_Iyy,RRT_Izz)

# In general, we store the inertia as dyadics, i.e. basis dependent tensors. 
# If you want to see what the inertia is expressed in a particular frame, use the to_matrix() method.

Chassis_dyadic.to_matrix(Chassis_frame)
RP_dyadic.to_matrix(RP_frame)
LUCA_dyadic.to_matrix(LUCA_frame)
RUCA_dyadic.to_matrix(RUCA_frame)
LLCA_dyadic.to_matrix(LLCA_frame)
RLCA_dyadic.to_matrix(RLCA_frame)
LSpdl_dyadic.to_matrix(LSpdl_frame)
RSpdl_dyadic.to_matrix(RSpdl_frame)
LTR_dyadic.to_matrix(LTR_frame)
RTR_dyadic.to_matrix(RTR_frame)
Hsg_dyadic.to_matrix(Hsg_frame)
LBC_dyadic.to_matrix(LBC_frame)
RBC_dyadic.to_matrix(RBC_frame)
LUB_dyadic.to_matrix(LUB_frame)
RUB_dyadic.to_matrix(RUB_frame)
LLB_dyadic.to_matrix(LLB_frame)
RLB_dyadic.to_matrix(RLB_frame)
Jbar_dyadic.to_matrix(Jbar_frame)
LFT_dyadic.to_matrix(LFT_frame)
RFT_dyadic.to_matrix(RFT_frame)
LRT_dyadic.to_matrix(LRT_frame)
RRT_dyadic.to_matrix(RRT_frame)

# We will also eventually need to know what point the inertia is defined with respect to. 
# In our case, we will simply define all inertia's about the mass center. We can store the
#  total information needed by PyDy in a tuple of an inertia Dyadic and a Point.

Chassis_central_inertia = (Chassis_dyadic,CoM_Chassis)
RP_central_inertia = (RP_dyadic,CoM_RP)
LUCA_central_inertia = (LUCA_dyadic,CoM_LUCA)
RUCA_central_inertia = (RUCA_dyadic,CoM_RUCA)
LLCA_central_inertia = (LLCA_dyadic,CoM_LLCA)
RLCA_central_inertia = (RLCA_dyadic,CoM_RLCA)
LSpdl_central_inertia = (LSpdl_dyadic,CoM_LSpdl)
RSpdl_central_inertia = (RSpdl_dyadic,CoM_RSpdl)
LTR_central_inertia = (LTR_dyadic,CoM_LTR)
RTR_central_inertia = (RTR_dyadic,CoM_RTR)
Hsg_central_inertia = (Hsg_dyadic,CoM_Hsg)
LBC_central_inertia = (LBC_dyadic,CoM_LBC)
RBC_central_inertia = (RBC_dyadic,CoM_RBC)
LUB_central_inertia = (LUB_dyadic,CoM_LUB)
RUB_central_inertia = (RUB_dyadic,CoM_RUB)
LLB_central_inertia = (LLB_dyadic,CoM_LLB)
RLB_central_inertia = (RLB_dyadic,CoM_RLB)
Jbar_central_inertia = (Jbar_dyadic,CoM_Jbar)
LFT_central_inertia = (LFT_dyadic,CoM_LFT)
RFT_central_inertia = (RFT_dyadic,CoM_RFT)
LRT_central_inertia = (LRT_dyadic,CoM_LRT)
RRT_central_inertia = (RRT_dyadic,CoM_RRT)

# Rigid Bodies
# To completely define a rigid body, the mass center point, the reference frame, 
# the mass, and the inertia defined about a point must be specified

Chassis = RigidBody('Chassis',CoM_Chassis,Chassis_frame,m_Chassis,Chassis_central_inertia)
RP = RigidBody('RP',CoM_RP,RP_frame,m_RP,RP_central_inertia)
LUCA = RigidBody('LUCA',CoM_LUCA,LUCA_frame,m_LUCA,LUCA_central_inertia)
RUCA = RigidBody('RUCA',CoM_RUCA,RUCA_frame,m_RUCA,RUCA_central_inertia)
LLCA = RigidBody('LLCA',CoM_LLCA,LLCA_frame,m_LLCA,LLCA_central_inertia)
RLCA = RigidBody('RLCA',CoM_RLCA,RLCA_frame,m_RLCA,RLCA_central_inertia)
LSpdl = RigidBody('LSpdl',CoM_LSpdl,LSpdl_frame,m_LSpdl,LSpdl_central_inertia)
RSpdl = RigidBody('RSpdl',CoM_RSpdl,RSpdl_frame,m_RSpdl,RSpdl_central_inertia)
LTR = RigidBody('LTR',CoM_LTR,LTR_frame,m_LTR,LTR_central_inertia)
RTR = RigidBody('RTR',CoM_RTR,RTR_frame,m_RTR,RTR_central_inertia)
Hsg = RigidBody('Hsg',CoM_Hsg,Hsg_frame,m_Hsg,Hsg_central_inertia)
LBC = RigidBody('LBC',CoM_LBC,LBC_frame,m_LBC,LBC_central_inertia)
RBC = RigidBody('RBC',CoM_RBC,RBC_frame,m_RBC,RBC_central_inertia)
LUB = RigidBody('LUB',CoM_LUB,LUB_frame,m_LUB,LUB_central_inertia)
RUB = RigidBody('RUB',CoM_RUB,RUB_frame,m_RUB,RUB_central_inertia)
LLB = RigidBody('LLB',CoM_LLB,LLB_frame,m_LLB,LLB_central_inertia)
RLB = RigidBody('RLB',CoM_RLB,RLB_frame,m_RLB,RLB_central_inertia)
Jbar = RigidBody('Jbar',CoM_Jbar,Jbar_frame,m_Jbar,Jbar_central_inertia)
LFT = RigidBody('LFT',CoM_LFT,LFT_frame,m_LFT,LFT_central_inertia)
RFT = RigidBody('RFT',CoM_RFT,RFT_frame,m_RFT,RFT_central_inertia)
LRT = RigidBody('LRT',CoM_LRT,LRT_frame,m_LRT,LRT_central_inertia)
RRT = RigidBody('RRT',CoM_RRT,RRT_frame,m_RRT,RRT_central_inertia)

# ______________________________________________________________________________________________________________________________
# Gravity
# Define the gravitational constant
g = symbols('g')

# Forces are bound vectors, i.e. they act on a point. We need a force with a magnitude
#   mg  acting in the negative  y  direction of the inertial reference frame

Chassis_grav_force_vec = -m_Chassis * g * inertial_frame.z
RP_grav_force_vec = -m_RP * g * inertial_frame.z
LUCA_grav_force_vec = -m_LUCA * g * inertial_frame.z
RUCA_grav_force_vec = -m_RUCA * g * inertial_frame.z
LLCA_grav_force_vec = -m_LLCA * g * inertial_frame.z
RLCA_grav_force_vec = -m_RLCA * g * inertial_frame.z
LSpdl_grav_force_vec = -m_LSpdl * g * inertial_frame.z
RSpdl_grav_force_vec = -m_RSpdl * g * inertial_frame.z
LTR_grav_force_vec = -m_LTR * g * inertial_frame.z
RTR_grav_force_vec = -m_RTR * g * inertial_frame.z
Hsg_grav_force_vec = -m_Hsg * g * inertial_frame.z
LBC_grav_force_vec = -m_LBC * g * inertial_frame.z
RBC_grav_force_vec = -m_RBC * g * inertial_frame.z
LUB_grav_force_vec = -m_LUB * g * inertial_frame.z
RUB_grav_force_vec = -m_RUB * g * inertial_frame.z
LLB_grav_force_vec = -m_LLB * g * inertial_frame.z
RLB_grav_force_vec = -m_RLB * g * inertial_frame.z
Jbar_grav_force_vec = -m_Jbar * g * inertial_frame.z
LFT_grav_force_vec = -m_LFT * g * inertial_frame.z
RFT_grav_force_vec = -m_RFT * g * inertial_frame.z
LRT_grav_force_vec = -m_LRT * g * inertial_frame.z
RRT_grav_force_vec = -m_RRT * g * inertial_frame.z

# Forces on Chassis Points
LFSpg_F = symbols('LFSpg_F')
RFSpg_F = symbols('RFSpg_F')
LRSpg_F = symbols('LRSpg_F')
RRSpg_F = symbols('RRSpg_F')
FifthSpg_F = symbols('FifthSpg_F')
SixthSpg_F = symbols('SixthSpg_F')
LFTeth_F = symbols('LFTeth_F')
RFTeth_F = symbols('RFTeth_F')
LRTeth_F = symbols('LRTeth_F')
LRTeth_F = symbols('LRTeth_F')
RRTeth_F = symbols('RRTeth_F')
LFShk_F = symbols('LFShk_F')
RFShk_F = symbols('RFShk_F')
LRShk_F = symbols('LRShk_F')
RRShk_F = symbols('RRShk_F')
FifthShk_F = symbols('FifthShk_F')
TracShk_F = symbols('TracShk_F')
Nine10Shk_F = symbols('Nine10Shk_F')





# Other forces






# Lateral accel, long accel, vertical accel on chassis
# long accel on housing
# Spring loads, quasi-static
# Shock loads, quasi-static
# Loads at tires?
# Loads through control arms, spindles, bars, tie rods, jbar?

# Torques
