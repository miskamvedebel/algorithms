def population(logs: list) -> int:

    population = {}
    for p in logs:
        birth, death = p
        for d in range(birth, death):

            if d not in population:
                population[d] = 0
            population[d] += 1
    return sorted(population.items(), key=lambda x: (-x[1], x[0]))[0][0]

if __name__ == '__main__':
    print(population([[1950,1961],[1960,1971],[1970,1981]]))