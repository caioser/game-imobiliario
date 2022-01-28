class Cadastro:
    def __init__(self):
        self.labels = ["name", "country", "price", "rent", "house", "hotel", "mortigage"]
        self.comp = ["bus", "navigation", "aviation", "railroad"]
        self.gi = 0
        self.board_places = []
        self.whiling()
        """
        test = [
            {"name":"Havana", "country":"Cuba", "price":150, "rent":[30,90,150,240], "house":45, "hotel":90, "mortigage":120}
        ]
        """
    def whiling(self):
        while len(input("continue?")) == 0:
            self.adc()
        else:
            self.writing()
            print(f"Have {len(self.board_places)} board places registereds")


    def adc(self):
        if len(input("is company (no='' / yes='.*'): ")) > 0:
            self.board_places.append({"name": f"{self.comp[self.gi]} company", "price":100, "mortigage":200})
            self.gi += 1
            print(self.board_places[-1])

        p = {key: input(f"{key}: ") for key in self.labels}
        p["rent"] = [int(el) for el in p["rent"].split(" ")]
        for i in ["price", "house", "hotel", "mortigage"]:
            p[i] = int(p[i])
        self.board_places.append(p)
        print(self.board_places[-1])

    def writing(self):
        with open("board_places.txt", "w") as output:
            output.write(str("[\n"))
            for el in self.board_places:
                output.write(f"{str(el)}\n")
            output.write(str("]"))


a = Cadastro()