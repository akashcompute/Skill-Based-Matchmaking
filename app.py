# Program for Skill based Matchmaking

import itertools  # standard library for iterating and creating combinations or permutations


# class for performing OOPs concepts
class SBM:

    # constructor for pre initialization
    def __init__(self):
        self.player_name_with_score = {}
        self.players_on_each_side = 0
        self.total_no_of_players = 0
        self.teamA = []
        self.teamB = []
        self.matches = {}
        self.sorted_players = []

    # function to print the players in sorted order of scores
    def output(self):
        try:
            print("Sorted List of players (best to worst):")
            print("_" * 30)
            print('{:15} ==> {:>10}'.format("Player name", "Score"))
            print("-" * 30)
            for name, score in sorted(self.player_name_with_score.items(), key=lambda item: item[1],
                                      reverse=True):  # sorting the list of players
                print('{:15} ==> {:10d}'.format(name, score))
                self.sorted_players.append(name)                #creates a copy of sorted players
            print("-" * 30)
        except Exception as e:
            print("Error encountered in output() function")
            print(e)
            exit()

    # function to create the matches
    def form_matches(self):

        # print(self.teamA)
        j = 0
        while j < len(self.teamA):  # stores all the matches for future removal of repeating match
            for lines_teamB in self.teamB[j]:
                self.matches[self.teamA[j]] = lines_teamB
            j += 1

        self.teamA = []
        self.teamB = []

        self.teamA = list(self.matches.keys())
        self.teamB = list(self.matches.values())

        for key in self.teamA:  # removes duplicate matches
            if key in self.teamB:
                index = self.teamB.index(key)
                del self.matches[self.teamA[index]]
                del self.teamA[index]
                del self.teamB[index]

        print("Matches played:")
        match = 0
        j = 0
        while j < len(self.teamA):
            print("Match " + str(match + 1) + ": " + str(self.teamA[j]) + " vs " + str(self.teamB[j]))
            match += 1
            j += 1

    # function to create teams for the match
    def create_team(self):
        try:
            if (self.total_no_of_players % 2 == 0) and (self.total_no_of_players > self.players_on_each_side):  # check if teams can be formed or not
                values = list(
                    itertools.combinations(self.sorted_players, self.players_on_each_side)
                )  # makes different combinations of all team players

                for i in range(len(values)):  # loop finds opponent team members
                    emp = []  # stores all the opponent teams to be played with; matches with the player in each index in "values"
                    j = -1
                    while j < len(values) - 1:
                        j += 1
                        if j == i:  # iterate and exclude the team playing in team A
                            self.teamA.append(values[i])
                            continue
                        flag = 0
                        for value in values[i]:  # for excluding the player if present in the tuple
                            if value not in values[j]:  # if all the current players not found in rest of the teams then increment else decrement
                                flag += 1
                            else:
                                flag -= 1
                        if flag == self.players_on_each_side:  # if all the players in team A not present in rest of the combinatio of teams then append
                            emp.append(values[j])
                    self.teamB.append(emp)
            else:
                if self.total_no_of_players >= self.players_on_each_side:
                    print("Number of players should be more than the no of team members. Cannot make teams")
                else:
                    print("Odd no of players. Cannot make teams")
                exit()
        except Exception as e:
            print("Error encountered inside create_team()")
            print(e)
            exit()

    # function to take inputs
    def takeinput(self):

        self.players_on_each_side = int(input("Enter number of players on each side: "))
        print(" **** Leave the player name blank when you are done adding player **** ")
        print("Enter player names with their score")
        self.total_no_of_players = 0

        while True:
            try:
                name = input("Name of player " + str(self.total_no_of_players + 1) + ": ")
                if name == "":
                    break
                score = int(input("Score: "))
                self.player_name_with_score[name] = score
                self.total_no_of_players += 1
            except Exception as e:
                print("Error encountered while taking values")
                print(e)
                exit()


# driver program
if __name__ == "__main__":
    try:
        obj = SBM()
        obj.takeinput()
        obj.output()
        obj.create_team()
        obj.form_matches()
    except Exception as e:
        print("Error encountered in driver program")
        print(e)
        exit()
