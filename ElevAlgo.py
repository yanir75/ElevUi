import builder


class ElevAlgo:
    def __init__(self, building, calls):
        self.building = builder.building_from_json(building)
        self.calls = builder.calls_from_CSV(calls)
        self.calls_of_elev = [[]]
        self.route = [[]]

    def empty_route(self, elev):
        el = self.building.getElev(elev)
        if el.state == 1:
            el.state = -1
        elif el.state == -1:
            el.state = 1
        for i in self.calls_of_elev[elev]:
            if el.state == 1 and i.src > el.pos and i.status != 1:
                self.route[elev].append(i.src)
                i.status = 1
            if el.state == 1 and i.dest > i.src > el.pos:
                self.route[elev].append(i.dest)
            if el.state == -1 and i.src < el.pos and i.status != 1:
                self.route[elev].append(i.src)
                i.status = 1
            if el.state == -1 and i.dest < i.src < el.pos:
                self.route[elev].append(i.dest)
            if i.status == 1 and el.state == 1 and i.dest > el.pos:
                self.route[elev].append(i.dest)
            if i.status == 1 and el.state == -1 and i.dest < el.pos:
                self.route[elev].append(i.dest)
            if el.state == 0:
                if i.src > el.pos:
                    self.route[elev].append(i.src)
                    el.state = 1
                elif i.src < el.pos:
                    self.route[elev].append(i.src)
                    el.state = -1
                else:
                    if i.dest > el.pos:
                        self.route[elev].append(i.dest)
                        el.state = 1
                    elif i.dest < el.pos:
                        self.route[elev].append(i.dest)
                        el.state = -1

    def fix_route(self, elev, call):
        el = self.building.getElev(elev)
        if el.pos < call.src and el.state == 1:
            self.route[elev].append(call.src)
        if el.pos < call.src < call.dest and el.state == 1:
            self.route[elev].append(call.dest)
        if el.pos > call.src and el.state == -1:
            self.route[elev].append(call.src)
        if el.pos > call.src > call.dest and el.state == -1:
            self.route[elev].append(call.dest)
