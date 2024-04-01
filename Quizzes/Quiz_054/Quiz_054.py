class rainDrops:
    def nour2(self, n: int):
        out = ''
        dict = {3: 'i',
                5: 'a',
                7: 'o'}
        for key, value in dict.items():
            out += (n % key == 0) * f'Pl{value}ng'

        out = str(n) * (len(out) == 0) or out

        return out

test1 = rainDrops()
print(test1.nour2(35*3))
print(test1.nour2(35))
print(test1.nour2(3))

def convert(number):
    rain = [(3, 'i'), (5, 'a'), (7, 'o')]
    out = [f"Pl{r}ng"* number % d == 0 for d, r in rain]
    return ''.join(out) or str(number)


