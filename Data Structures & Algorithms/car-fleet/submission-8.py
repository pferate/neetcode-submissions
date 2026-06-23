from collections import defaultdict, deque


class Fleet:
    def __init__(self, position: int, speed: int) -> None:
        self.position = position
        self.speed = speed
        self.reached_at = 0
    
    def increment(self) -> None:
        self.position += self.speed
    
    def __repr__(self):
        return f"Fleet(pos:{self.position}, spd:{self.speed})"


class Fleets:
    def __init__(self, target: int, position: List[int], speed: List[int]) -> None:
        self.target = target
        # Temporary object, used so we can sort by position, but not lose the index for speed
        self._traveling_fleet_dict = defaultdict(int)
        for i, pos in enumerate(position):
            self._traveling_fleet_dict[pos] = speed[i]
        # Collection of Fleets, sorted by position
        self.traveling_fleets = deque()
        for pos, speed in sorted(self._traveling_fleet_dict.items(), reverse=True):
            self.traveling_fleets.append(Fleet(pos, speed))
        # Fleets that have reached the target
        self.completed_fleets = []
    
    def increment_all(self) -> None:
        # print(f"Before: {self.traveling_fleets}")
        new_fleets = deque()
        for i, fleet in enumerate(self.traveling_fleets):
            # print(f"Incrementing fleet: {fleet} -> ", end="")
            fleet.increment()
            # print(fleet)
            # Which point of the hour the target was reached
            if self.target <= fleet.position:
                fleet.reached_at = 1 - ((fleet.position - self.target) / fleet.speed)
                # print(f"Fleet reached target at: {fleet.reached_at}")

            # Add the first car to the fleet
            if len(new_fleets) == 0:
                # print(f"Adding first fleet: {fleet}")
                new_fleets.append(fleet)
            # If this fleet's new position is behind the last in the new fleet list, then append it
            elif fleet.position < new_fleets[-1].position:
                # print(f"Appending fleet (1): {fleet}")
                new_fleets.append(fleet)
            # If this fleet reached the target after the previous fleet, append it
            elif new_fleets[-1].reached_at < fleet.reached_at:
                # print(f"Appending fleet (2): {fleet}")
                new_fleets.append(fleet)
            # # If the previous fleet has passed (not just reached) the target
            # # AND this fleet has passed (not just reached) the target
            # # THEN also append it
            # elif self.target < new_fleets[-1].position  and self.target < fleet.position:
            #     # print(f"Appending fleet (3): {fleet}")
            #     new_fleets.append(fleet)
            # Otherwise, we would meet up with the last car and merge into that fleet, so do nothing
            # else:
            #     print(f"Merging fleet: {fleet}")
        self.traveling_fleets = new_fleets
        # print(f"After: {self.traveling_fleets}")
        while len(self.traveling_fleets) > 0 and self.traveling_fleets[0].position >= self.target:
            # print(f"Fleet reached target ({self.target}): {fleet}")
            finished_fleet = self.traveling_fleets.popleft()
            self.completed_fleets.append(finished_fleet)
            

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        all_fleets = Fleets(target, position, speed)
        while all_fleets.traveling_fleets:
            # print(f"Traveling.\n\ttraveling_fleets ({len(all_fleets.traveling_fleets)}): {all_fleets.traveling_fleets},\n\tcompleted_fleets ({len(all_fleets.completed_fleets)}): {all_fleets.completed_fleets}")
            all_fleets.increment_all()
        return len(all_fleets.completed_fleets)
