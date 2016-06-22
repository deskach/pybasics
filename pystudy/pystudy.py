from resolver import *

def chap2():
    resolve = resolver.Resolver()

    print(resolve('tut.by'))
    print(resolve('lenta.ru'))
    print(resolve.has_host('tut.by'))
    resolve.clear()
    print(resolve.has_host('tut.by'))

    seq = resolver.sequence_class(False)
    print(seq("12345"))

    scientists = ['Marie Curie', 'Albert Einstein',
                  'Neils Bohr', 'Isaac Newton']
    last_name = lambda name: name.split()[-1]
    print(sorted(scientists, key=last_name))
    print(last_name('Nikila Tesla'))
    print("Callable(last_name)=%s" % (callable(last_name)))

    print(resolver.hypervolume(1,2,3,4))
    lengths = [1,2,3]
    print(resolver.hypervolume(*lengths))

    print(resolver.tag('img', src="son.jpg", alt="Tolia"))

    sun = (10, 20, 30, 40)
    mon = (11, 21, 31, 41)
    tue = (12, 32, 22, 33)
    combined = [item for item in zip(sun, mon, tue)]
    print(combined)

if __name__ == "__main__":
    chap2()