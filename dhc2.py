from ti_system import disp_clr

front=0
centre=0
rear=0
ltip=0
rtip=0

tips=False
empty_wt=0
empty_arm=0
fuel_dens=6.0

fuel_unit="USG"
USG_PER_IMP=1.20095
USG_PER_LTR=0.264172

pilot=0
row2=0
row3=0
baggage=0

# --- PLACEHOLDER DATA - VERVANG MET POH WAARDEN ---
MAX_GROSS_WT=5370.0
CG_FWD_LIMIT=85.0
CG_AFT_LIMIT=95.0

FUEL_ARM_FRONT=20.0
FUEL_ARM_CENTRE=45.0
FUEL_ARM_REAR=70.0
FUEL_ARM_LTIP=55.0
FUEL_ARM_RTIP=55.0

PILOT_ARM=85.0
ROW2_ARM=118.0
ROW3_ARM=150.0
BAGGAGE_ARM=178.0
# --- EINDE PLACEHOLDER DATA ---

def usg_to_unit(usg,unit):
    if unit=="IMP":
        return usg/USG_PER_IMP
    elif unit=="LTR":
        return usg/USG_PER_LTR
    else:
        return usg

def unit_to_usg(val,unit):
    if unit=="IMP":
        return val*USG_PER_IMP
    elif unit=="LTR":
        return val*USG_PER_LTR
    else:
        return val

def menu():
    while True:
        disp_clr()
        print("DHC-2 BEAVER")
        print("WEIGHT & BALANCE")
        print("----------------")
        print("1. FUEL LOAD")
        print("2. CABIN LOAD")
        print("3. AIRCRAFT SETTINGS")
        print("4. GENERATE W&B")
        print("5. QUIT")

        c=input("SELECT: ")

        if c=="1":
            fuel_menu()
        elif c=="2":
            cabin_menu()
        elif c=="3":
            settings()
        elif c=="4":
            generate()
        elif c=="5":
            disp_clr()
            return

def settings():
    global tips,empty_wt,empty_arm,fuel_dens

    while True:
        disp_clr()
        print("AIRCRAFT SETTINGS")
        print("----------------")
        print("1. EMPTY WEIGHT")
        print("2. EMPTY ARM")

        if tips:
            print("3. TIP TANKS: YES")
        else:
            print("3. TIP TANKS: NO")

        print("4. FUEL DENSITY")
        print("5. SHOW SETTINGS")
        print("6. RETURN")

        c=input("SELECT: ")

        if c=="1":
            disp_clr()
            print("EMPTY WEIGHT - LB")
            empty_wt=float(input("WEIGHT: "))

        elif c=="2":
            disp_clr()
            print("EMPTY ARM - IN")
            empty_arm=float(input("ARM: "))

        elif c=="3":
            tips=not tips

        elif c=="4":
            disp_clr()
            print("FUEL DENSITY")
            print("LB / USG")
            fuel_dens=float(input("VALUE: "))

        elif c=="5":
            show_settings()

        elif c=="6":
            return

def show_settings():
    disp_clr()
    print("AIRCRAFT SETTINGS")
    print("----------------")
    print("EMPTY WT:",empty_wt)
    print("EMPTY ARM:",empty_arm)

    if tips:
        print("TIP TANKS: YES")
    else:
        print("TIP TANKS: NO")

    print("FUEL:",fuel_dens,"LB/USG")
    input("ENTER")

def fuel_menu():
    global front,centre,rear,ltip,rtip,fuel_unit

    while True:
        disp_clr()
        print("FUEL LOAD")
        print("----------------")
        print("1. UNITS:",fuel_unit)
        print("2. FRONT:",round(usg_to_unit(front,fuel_unit),1))
        print("3. CENTRE:",round(usg_to_unit(centre,fuel_unit),1))
        print("4. REAR:",round(usg_to_unit(rear,fuel_unit),1))

        if tips:
            print("5. L TIP:",round(usg_to_unit(ltip,fuel_unit),1))
            print("6. R TIP:",round(usg_to_unit(rtip,fuel_unit),1))
            print("7. RETURN")
        else:
            print("5. RETURN")

        c=input("SELECT: ")

        if c=="1":
            if fuel_unit=="USG":
                fuel_unit="IMP"
            elif fuel_unit=="IMP":
                fuel_unit="LTR"
            else:
                fuel_unit="USG"

        elif c=="2":
            disp_clr()
            print("FRONT TANK -",fuel_unit)
            front=unit_to_usg(float(input("QTY: ")),fuel_unit)

        elif c=="3":
            disp_clr()
            print("CENTRE TANK -",fuel_unit)
            centre=unit_to_usg(float(input("QTY: ")),fuel_unit)

        elif c=="4":
            disp_clr()
            print("REAR TANK -",fuel_unit)
            rear=unit_to_usg(float(input("QTY: ")),fuel_unit)

        elif c=="5" and tips:
            disp_clr()
            print("L TIP TANK -",fuel_unit)
            ltip=unit_to_usg(float(input("QTY: ")),fuel_unit)

        elif c=="5" and not tips:
            return

        elif c=="6" and tips:
            disp_clr()
            print("R TIP TANK -",fuel_unit)
            rtip=unit_to_usg(float(input("QTY: ")),fuel_unit)

        elif c=="7" and tips:
            return

def cabin_menu():
    global pilot,row2,row3,baggage

    while True:
        disp_clr()
        print("CABIN LOAD - LB")
        print("----------------")
        print("1. PILOT+FRONT:",pilot)
        print("2. ROW 2:",row2)
        print("3. ROW 3:",row3)
        print("4. BAGGAGE:",baggage)
        print("5. RETURN")

        c=input("SELECT: ")

        if c=="1":
            disp_clr()
            print("PILOT + FRONT PAX - LB")
            pilot=float(input("WEIGHT: "))

        elif c=="2":
            disp_clr()
            print("ROW 2 PAX - LB")
            row2=float(input("WEIGHT: "))

        elif c=="3":
            disp_clr()
            print("ROW 3 PAX - LB")
            row3=float(input("WEIGHT: "))

        elif c=="4":
            disp_clr()
            print("BAGGAGE - LB")
            baggage=float(input("WEIGHT: "))

        elif c=="5":
            return

def generate():
    if tips:
        fuel_usg=front+centre+rear+ltip+rtip
    else:
        fuel_usg=front+centre+rear

    fuel_wt=fuel_usg*fuel_dens
    cabin_wt=pilot+row2+row3+baggage
    total_wt=empty_wt+fuel_wt+cabin_wt

    moment=empty_wt*empty_arm
    moment=moment+front*fuel_dens*FUEL_ARM_FRONT
    moment=moment+centre*fuel_dens*FUEL_ARM_CENTRE
    moment=moment+rear*fuel_dens*FUEL_ARM_REAR

    if tips:
        moment=moment+ltip*fuel_dens*FUEL_ARM_LTIP
        moment=moment+rtip*fuel_dens*FUEL_ARM_RTIP

    moment=moment+pilot*PILOT_ARM
    moment=moment+row2*ROW2_ARM
    moment=moment+row3*ROW3_ARM
    moment=moment+baggage*BAGGAGE_ARM

    if total_wt>0:
        cg=moment/total_wt
    else:
        cg=0

    disp_clr()
    print("GENERATE W&B")
    print("----------------")
    print("EMPTY WT:",round(empty_wt,1))
    print("FUEL WT:",round(fuel_wt,1))
    print("CABIN WT:",round(cabin_wt,1))
    print("TOTAL WT:",round(total_wt,1))
    print("CG:",round(cg,2),"IN")
    input("ENTER")

    disp_clr()
    print("GENERATE W&B")
    print("----------------")

    if total_wt>MAX_GROSS_WT:
        print("OVER MAX WEIGHT!")
        print("MAX:",MAX_GROSS_WT,"LB")
    else:
        print("WEIGHT: OK")

    if cg<CG_FWD_LIMIT or cg>CG_AFT_LIMIT:
        print("CG OUT OF LIMITS!")
        print(CG_FWD_LIMIT,"-",CG_AFT_LIMIT,"IN")
    else:
        print("CG: OK")

    input("ENTER")
    
# Main Program
menu()