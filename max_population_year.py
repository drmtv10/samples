#!/bin/python
# find max population year, given a list of people, birth year and death year.

# run time for this implementation:
# year->population count O(p) - p = persons
# min_year -> max_year iteration loop O(y)
# so total run time - O(p+y), which seems comparable to one
# mentioned in Java implementation that builds get_Deltas and then adds
# deltas for each entry, going from min to max year.
def calc_max_population(pbdy=None):
    """
    input = pbdy - population year - list of people, birth and death year
    return - year when population is max
    """
    population_year = dict()
    max_population = population = 0
    max_py = 0
    min_year = max_year = 0
    for pbdy_entry in pbdy:
        (pname,birthyear,deathyear) = pbdy_entry.split()
        by = int(birthyear)
        dy = int(deathyear)
        # build map of year -> population count
        if by in population_year:
            population_year[by] += 1
        else:
            population_year[by] = 1
        if dy in population_year:
            population_year[dy] -= 1
        else:
            population_year[dy] = -1
        #print population_year
        # keep track of min / max year in population count map
        if min_year == 0:
            min_year = by
        elif by < min_year:
            min_year = by
        if max_year == 0:
            max_year = dy
        elif max_year < by:
            max_year = by
        elif max_year < dy:
            max_year = dy
        #print min_year, max_year
    # Calculate max population by counting population between
    # min_year -> max_year
    for year in range(min_year, max_year):
        if year in population_year:
            population += population_year[year]
            if max_population < population:
                max_population = population
                max_py = year
        #print year, population, max_py, max_population

    return max_py

if __name__ == '__main__':
    person_birth_death_rec = [ 'a1 1950 2000',
                               'a2 1942 2001',
                               'a3 1921 1995',
                               'a4 1960 1991',
                               'a5 1942 2005',
                               'a6 2001 2018',
                               'a7 1982 2002',
                               'a8 1976 1990',
                               'a9 1942 2030',
                               ]
    max_population_year = calc_max_population(person_birth_death_rec)
    print max_population_year

        
            
