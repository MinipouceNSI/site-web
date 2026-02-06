def fusion(lsta, lstb) :
    """
    si lsta et lstb 
    la fonction retourne une liste triée des deux listes
    """
    i = 0
    j = 0
    reponse = []
    while i < len(lsta) and j < len(lstb) :
            if lsta[i] <= lstb[j] :
                reponse.append(lsta[i])
                i += 1
            else :
                reponse.append(lstb[j])
                j += 1
    if i == len(lsta) :
        while j < len(lstb) : 
            reponse.append(lstb[j])
    else :
        while i < len(lsta) :
            reponse.append(lstb[i])
    return reponse

    #test
    assert fusion([3,4,5], [3, 4, 7, 9]) == [3, 3, 4, 4, 5, 7, 9]