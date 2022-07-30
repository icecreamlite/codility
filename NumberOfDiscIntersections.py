"""
Count the circle that opens and when a circle closed, all of the current open intersects that
circle that closes (except itself, thus the minus 1)
"""

def solution(A):
    opening, closing = [], []
    
    for center, rad in enumerate(A):
        opening.append(center - rad)
        closing.append(center + rad)

    opening.sort()
    closing.sort()

    disc_intersection = 0
    indop = 0

    for indcl, cl in enumerate(closing):

        while indop < len(opening) and opening[indop] <= cl: # count all open until one closed
            indop += 1

        # all current open intersects the circle that closed (excluding itself)
        disc_intersection += indop - indcl - 1

        if disc_intersection > 10000000:
            return -1

    return disc_intersection