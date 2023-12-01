class Crt:
    def __init__(self, cycles, display):
        self.cycles = cycles
        self.display = display
        self.clock_cycle = 1
        self.xreg = 1
        self.crt_horizontal_pos = 0

    def tik(self):
        if self.display: self.draw()
        if self.clock_cycle in self.cycles:
            self.cycles[self.clock_cycle] = self.clock_cycle * self.xreg
            if self.display: print() # Next row in CRT
            self.crt_horizontal_pos = 0
        else:
            self.crt_horizontal_pos += 1
        self.clock_cycle += 1

    def draw(self):
        if self.xreg >= self.crt_horizontal_pos-1 and self.xreg <= self.crt_horizontal_pos+1:
            # Beam within sprite position
            print("#", end="")
        else:
            # Beam outside sprite position
            print(".", end="")

    def noop(self, param=None):
        self.tik()
        
    def addx(self, param):
        self.tik()
        self.tik()
        self.xreg += param
 
    def exec(self, instr, value = None):
        getattr(self, instr)(value)

def quiz(input, cycles, display):
    crt = Crt(cycles, display)
    with open(input) as file:
        for line in file:
            line = line.replace("\n", "")
            parts = line.split()
            if len(parts) == 2:
                instr, param = parts
                crt.exec(instr, int(param))
            else:
                crt.exec(parts[0])
    if not display: print("\nTotal CRT strength is "+str(sum(crt.cycles.values())))

def main():
    quiz("day10/input.txt", { 20: 0, 60: 0, 100:0, 140:0 ,180:0 ,220:0 }, False) # Part 1
    quiz("day10/input.txt", { 40: 0, 80: 0, 120:0, 160:0 ,200:0 ,240:0 }, True)  # Part 2

if __name__ == "__main__":
    main()
