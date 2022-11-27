import random
def generateSchedule(_shipsNumber):
    for i in range(_shipsNumber):
        schedule.append({"day": random.randint(1, 31), "hour": random.randint(0, 24), "minutes": random.randint(0, 60),
                         "ship": random.choice(ship_names), "cargoType": random.choice(cargo_types),
                         "weight": random.randint(5000, 30000)})

def acceptNewShip(_schedule):
    for i in range(len(_schedule)):
        if _schedule[i]["day"] == day and _schedule[i]["hour"] == hour and _schedule[i]["minutes"] == minutes:
            arrived.append(schedule[i])
def startUnloading(_arrived):
    for j in range(len(_arrived)):
        if len(CONT_CRANE) == 0 and _arrived[j]["cargoType"] == "CONT":
            CONT_CRANE.append(_arrived[j])
            del _arrived[j]

        elif len(LIQ_CRANE) == 0 and _arrived[j]["cargoType"] == "LIQ":
            LIQ_CRANE.append(_arrived[j])
            del _arrived[j]

        elif len(BULK_CRANE) == 0 and _arrived[j]["cargoType"] == "BULK":
            BULK_CRANE.append(_arrived[j])
            del _arrived[j]


ship_names = ["KSL-SANTOS", "VITAOCEAN", "SEA AMETHYST", "MSC BENEDETTA"
              "BLUE SEA", "ZENOVIA LADY", "MARLIN AMBER", "ALPHA UNITY",
              "SHANDONG JUNIPER", "GISELA OLDENDORFF", "MSC SVEVA",
              "MSC GENEVA", "MSC LEIGH", "GSL CHATEAU DIF", "LR1 CARRIER",
              "MATALA", "BBC NEPTUNE", "WULIN", "ATLANTIC SILVER",
              "CAP SAN TAINARO", "FRIO FORWIN", "SHANDONG FU DE"]
cargo_types = ["CONT", "LIQ", "BULK"]


schedule = []
arrived = []



#cranes available
CONT_CRANE = []
LIQ_CRANE = []
BULK_CRANE = []

generateSchedule(15)


for day in range(31):
    for hour in range(0, 24):
        for minutes in range(0, 60):
            acceptNewShip(schedule)
        startUnloading(arrived)



print("Currently unloading: ")
print()
for ship in CONT_CRANE:
    print(
        f'{ship["day"]} DAY {ship["hour"]}:{ship["minutes"]} "{ship["ship"]}" {ship["cargoType"]} {ship["weight"]} tonne is being unloaded')
for ship in LIQ_CRANE:
    print(
        f'{ship["day"]} DAY {ship["hour"]}:{ship["minutes"]} "{ship["ship"]}" {ship["cargoType"]} {ship["weight"]} tonne is being unloaded')
for ship in BULK_CRANE:
    print(
        f'{ship["day"]} DAY {ship["hour"]}:{ship["minutes"]} "{ship["ship"]}" {ship["cargoType"]} {ship["weight"]} tonne is being unloaded')

print()
print("Currently in queue: ")
print()
for ship in arrived:
    if ship["cargoType"] == "CONT":
        print(f'{ship["day"]} DAY {ship["hour"]}:{ship["minutes"]} "{ship["ship"]}" {ship["cargoType"]} {ship["weight"]} tonne -> CONT_CRANE')
    elif ship["cargoType"] == "LIQ":
        print(f'{ship["day"]} DAY {ship["hour"]}:{ship["minutes"]} "{ship["ship"]}" {ship["cargoType"]} {ship["weight"]} tonne -> LIQ_CRANE')
    elif ship["cargoType"] == "BULK":
        print(f'{ship["day"]} DAY {ship["hour"]}:{ship["minutes"]} "{ship["ship"]}" {ship["cargoType"]} {ship["weight"]} tonne -> BULK_CRANE')

