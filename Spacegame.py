import random

# ========================================================================================================================================================
# GALAXY CLASS
# ========================================================================================================================================================

class Galaxy:

    maxStars = 25000


    def __init__(self):
        self.name = "Milky Way"
        self.stars = []
        numberOfStars = random.randint(0, Galaxy.maxStars)
        for i in range(int(numberOfStars / 5), numberOfStars):
            self.stars.append(Star())
    
    def toString(self):
        outString = ""
        outString += "Name: " + self.name
        for i in self.stars:
            outString += i.toString()
        return outString

    def getRandomStarIndex(self):
        randomStar = random.randint(0, len(self.stars) -1 )
        return randomStar

# ========================================================================================================================================================
# STAR CLASS
# ========================================================================================================================================================


class Star:

    total = 0

    minTemp = 2400
    maxTemp = 90000
    maxPlanets = 15
    sunDiameter = 1391016
    
    prefixList = ["NGC-", "HD ", "WISE ", "Gilese "]
    classList = ["O", "B", "A", "F", "G", "K", "M"]

    def __init__(self, name=None):
        Star.total += 1

        # GENERATING PLANETS:
        self.planets = []
        self.numberOfPlanets = random.randint(1, Star.maxPlanets)
        for i in range(0, self.numberOfPlanets):
            self.planets.append(Planet())
        
        # CREATING SYSTEM NAME:
        if name==None:
            prefix = Star.prefixList[random.randint(0, len(Star.prefixList) - 1)]
            if prefix == "NGC":
                suffix = random.randint(1, 7840)
            else:
                suffix = random.randint(10000, 99999)
            self.name = prefix + str(suffix)
        else:
            self.name = name
        
        # DETERMINING SYSTEM CLASS + TEMPERATURE:
        classifier = random.randint(0, 10000)
        if classifier <= 13:
            self.starClass = Star.classList[1]
            self.temp = random.randint(10001, 30000)
            self.color = "Blue"
        elif classifier <= 73:
            self.starClass = Star.classList[2]
            self.temp = random.randint(7501, 10000)
            self.color = "White"
        elif classifier <= 360:
            self.starClass = Star.classList[3]
            self.temp = random.randint(6001, 7500)
            self.color = "White"
        elif classifier <= 820:
            self.starClass = Star.classList[4]
            self.temp = random.randint(5201, 6000)
            self.color = "Yellow"
        elif classifier <= 2030:
            self.starClass = Star.classList[5]
            self.temp = random.randint(3701, 5200)
            self.color = "Yellow"
        elif classifier <= 9999:
            self.starClass = Star.classList[6]
            self.temp = random.randint(2400, 3700)
            self.color = "Red"
        else:
            self.starClass = Star.classList[0]
            self.temp = random.randint(30001, 250000)
            self.color = "Blue"
        
        classifier = random.randint(1, 381)
        if classifier <= 25:
            self.size = random.randint(int(.02 * Star.sunDiameter), int(.25 * Star.sunDiameter))
            self.sizeClass = "Dwarf"
        elif classifier <= 200:
            self.size = random.randint(int(.25 * Star.sunDiameter), 2 * Star.sunDiameter)
            self.sizeClass = "Main Sequence"
        elif classifier <= 300:
            self.size = random.randint(2 * Star.sunDiameter, 4 * Star.sunDiameter)
            self.sizeClass = "Main Sequence"
        elif classifier <= 350:
            self.size = random.randint(4 * Star.sunDiameter, 6 * Star.sunDiameter)
            self.sizeClass = "Supergiant"
        elif classifier <= 375:
            self.size = random.randint(6 * Star.sunDiameter, 8 * Star.sunDiameter)
            self.sizeClass = "Supergiant"
        else:
            self.sizeClass = "Hypergiant"
            self.size = random.randint(8 * Star.sunDiameter, 2000 * Star.sunDiameter)

        

    def toString(self):
        outString = ""
        outString += "Name: " + self.name
        outString += "\nTemperature: {:,} K".format(self.temp)
        outString += "\nDiameter: {:,} km".format(self.size)
        outString += "\nPlanets: " + str(len(self.planets))
        outString += "\nClass: {}".format(self.starClass)
        outString += "\n{0} {1} Star \n\n\tPlanets:\n".format(self.color, self.sizeClass)
        for i in self.planets:
            outString += "\n" + i.toString() + "\n"
        return outString


    def getRandomPlanetIndex(self):
        randomPlanet = random.randint(0, len(self.planets) -1 )
        return randomPlanet

# ========================================================================================================================================================
# PLANET CLASS
# ========================================================================================================================================================


class Planet:
    
    total = 0
    totalHabitable = 0
    totalInhabited = 0

    typeList = ["Terrestrial", "Gas Giant", "Water World", "Dwarf Planet"]
    minSize = 1000
    maxSize = 150000
    maxMoons = 3

    # INITIALIZING PLANET:
    # IF GIVEN ARGS:
    #       REQUIRES NAME, SIZE, TYPE, AND HABITABILITY
    def __init__(self, name=None, size=None, typ=None, habitable=None):

        self.controlled = False
        # IF NO ARGUMENTS ARE GIVEN
        # GENERATE A RANDOM PLANET:
        if name==None:
            self.name = "P-{:}".format(Planet.total)
            self.size = random.randint(Planet.minSize, Planet.maxSize)

            # DETERMINING TYPE OF PLANET:
            if self.size >= 100000:
                self.typ = "Gas Giant"
            elif self.size >= 50000:
                self.typ = "Water World"
            elif self.size >= 4000:
                self.typ = "Terrestrial"
            else:
                self.typ = "Dwarf Planet"
            
            # GENERATING MOONS:
            self.moons = []
            self.numberOfMoons = random.randint(1, Planet.maxMoons)
            for i in range(0, self.numberOfMoons):
                self.moons.append(Moon(self.size, True))


            # DETERMINING HABITABILITY OF PLANET:
            self.habitable = False
            if self.typ == "Terrestrial" and self.numberOfMoons == 1:
                if random.randint(0, 5) == 1:
                    self.habitable = True
                    Planet.totalHabitable += 1
        

        # ONLY TRIGGERS IF THE PLANET IS GIVEN ARGUMENTS
        # IF SO, IT ASSIGNS THEM TO INSTANCE-VARIABLES.
        else:
            self.name = name
            self.size = size
            self.typ = typ
            self.habitable = habitable
            self.moons = []
        Planet.total += 1
        

    # EXTRACTS RESOURCES FROM PLANET FOR PLAYER
    # ALSO EXTRACTS ANYTHING FROM MOONS ORBITING PLANET
    def extract(self):
        global silicon
        global iron
        global fuel
    

    # RETURNS STRING OF INFORMATION ABOUT PLANET
    # HABITABILITY, NAME, SIZE, MOONS, ETC.
    def toString(self):
        if self.habitable:
            habitability = 'Habitable'
        else:
            habitability = 'Non-Habitable'
        outString = ""
        outString += "\tName: " + self.name
        outString += "\n\tDiameter: {:,} Km".format(self.size)
        outString += "\n\tMoons: " + str(len(self.moons))
        outString += "\n\tType: " + habitability + ', ' + self.typ

        # for idx, i in enumerate(self.moons):
        #     outString += "\n\n\t\tMoon #" + str(idx + 1)
        #     outString += "\n\t\tDiameter: {:,} Km".format(i.size) 

        return outString
            

# ========================================================================================================================================================
# MOON CLASS
# ========================================================================================================================================================

class Moon:

    total = 0

    def __init__(self, size, planetSize):
        if planetSize:
            self.size = random.randint(int(size * .001), int(size * .04))
        else:
            self.size = size
        Moon.total += 1

# ========================================================================================================================================================
# CIV CLASS
# ========================================================================================================================================================

class Civ:
    total = 0

    # THE ODDS OF A CIVILIZATION SPREADING ARE 1 IN chanceToSpread.
    chanceToSpread = 3

    def __init__(self):
        Civ.total += 1
        self.planetsControlled = []
        while True:
            self.hs = galaxy.getRandomStarIndex()
            self.hw = [self.hs, galaxy.stars[self.hs].getRandomPlanetIndex()]
            if galaxy.stars[self.hw[0]].planets[self.hw[1]].habitable:
                self.inhabitPlanet(self.hw)
                break
    
    def inhabitPlanet(self, coords):
        Planet.totalInhabited += 1

        # SET PLANET'S STATE TO CONTROLLED:
        planetToInhabit = getCoordinate(coords)
        planetToInhabit.controlled = True
        setCoordinate(coords, planetToInhabit)

        # ADD COORDINATE TO CONTROLLED PLANETS:
        self.planetsControlled.append(coords)


# ========================================================================================================================================================
# THE REST OF THE CODE:
# ========================================================================================================================================================

userIn = ''
gameLoop = True

# # GENERATING EARTH:
# planetList = [Planet('Earth', 12742, 'Basic', True)]
# planetList[0].moons.append(Moon(1737, False))


def getCoordinate(coords):
    return galaxy.stars[coords[0]].planets[coords[1]]


def setCoordinate(coords, planet):
    galaxy.stars[coords[0]].planets[coords[1]] = planet


def advanceTurn():
    for i in civs:
        spread = random.randint(1, Civ.chanceToSpread)
        if spread == 1:
            i.inhabitPlanet([0,0])


while True:
    input("Press ENTER to generate a new system")
    print("\n\nGenerating...\n\n")
    
    civs = []
    galaxy = Galaxy()

    print("\n\nDone!  Finding home system...\n\n")
    
    civs.append(Civ())

    print("HOMEWORLD:")
    print("----------")
    print("Coordinates: " + str(civs[0].hw))
    print("")
    print(getCoordinate(civs[0].hw).toString())
    print("\n")


    while True:
        print("GALAXY STATISTICS:")
        print("------------------")
        print("Stars: {:,}".format(Star.total))
        print("Planets: {:,} | Habitable: {:,} | Inhabited: {:,}".format(Planet.total, Planet.totalHabitable, Planet.totalInhabited))
        print("Moons: {:,}".format(Moon.total))
        print()
        print("\nOPTIONS:\n--------")
        input("Press enter to advance one turn.")
        advanceTurn()
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    