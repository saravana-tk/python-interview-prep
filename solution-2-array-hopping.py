'''
Alice loves to play a jumping game on two parallel roads, roadA and roadB, each filled with integers. The game begins with Alice choosing a starting point on roadA, and then moving according to the following rules:

Alice chooses a starting point on roadA.
Each element in both the roads dictate exactly where to jump on the other road. If Alice is at the 
i
i-th position of roadA, where roadA[
i
i] = 
x
x, then Alice moves to the 
x
x-th position of roadB. Likewise, if Alice is at the 
i
i-th position of roadB, where roadB[
i
i] = 
y
y, then she moves to the 
y
y-th position of roadA.
Alice continues these jumps until she ends up at an already visited spot on either road in the current route, which signifies the end of this game. It's important to note that if a spot was visited in a previous route but not in the current route, it is not considered as an already visited spot.
The distance covered in each jump is defined as 1 unit, no matter where she jumps to on the other road.
Your task is to create a function that receives these two roads, roadA and roadB, as its parameters. The function should calculate and return an array of total distances Alice covers during her game for each possible starting point on roadA. More specifically, the result should be an array results, where results[i] denotes the total distance covered if Alice starts from roadA[i].

The two input lists, roadA and roadB, contain 
n
n and 
m
m number of elements respectively. The number of elements in each list can range from 1 to 100, inclusive. Each element in roadA can have a value ranging from 0 to 
m
−
1
m−1, inclusive. Similarly, each element in roadB can have a value ranging from 0 to 
n
−
1
n−1, inclusive. This ensures that any element in either of the lists will be a valid index in the other list.

Example

For instance, if Alice's roads are given as roadA = [1, 0, 2] and roadB = [2, 0, 1], the function should return [2, 4, 4] because:

If Alice starts from roadA[0], her first jump takes her to roadB[1]. The value at this index tells her to jump to roadA[0], but since that's where she started this route (and thus it's already visited), she stops. As a result, Alice covers a total distance of 2 units.

If Alice starts from roadA[1], she jumps to roadB[0] which then redirects her to roadA[2]. From roadA[2], she jumps to roadB[1] which then leads her to roadA[0]. From roadA[0], she jumps to roadB[1] again but realizes this is the spot she has already visited in this route. Thus, in this case she covers a total distance of 4 units.

If Alice starts from roadA[2], her first jump takes her to roadB[2] and then the rule at this position directs her to roadA[1]. She has not yet visited roadA[1] in this route, so she follows the instruction and jumps to roadB[0], which also directs her to roadA[2], which she has visited in this route already so she stops there. Therefore, she covers a total distance of 4 units before landing on an already visited spot in her current route.
'''
def solution(roadA, roadB):
    final_list = []
    for index in range(len(roadA)):
        roadAVisited, roadBVisited = set(), set()
        visitCount = 0
        while True:
            if index in roadAVisited:
                break
            roadAVisited.add(index)
            visitCount += 1
            index = roadA[index]
            if index in roadBVisited:
                break
            roadBVisited.add(index)
            visitCount += 1
            index = roadB[index]
        final_list.append(visitCount)
    return final_list