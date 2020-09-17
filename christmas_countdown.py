from datetime import date
from datetime import datetime

LETTERS = {
    "a": ["###", "# #", "###", "# #", "# #"],
    "b": ["###", "# #", "###", "# #", "###"],
    "c": ["###", "#  ", "#  ", "#  ", "###"],
    "d": ["## ", "# #", "# #", "# #", "## "],
    "e": ["###", "#  ", "###", "#  ", "###"],
    "f": ["###", "#  ", "###", "#  ", "#  "],
    "g": ["###", "# #", "###", "  #", "###"],
    "h": ["# #", "# #", "###", "# #", "# #"],
    "i": ["###", " # ", " # ", " # ", "###"],
    "j": ["###", "  #", "  #", "  #", "## "],
    "k": ["# #", "## ", "#  ", "## ", "# #"],
    "l": ["#  ", "#  ", "#  ", "#  ", "###"],
    "m": ["# #", "###", "###", "# #", "# #"],
    "n": ["###", "# #", "# #", "# #", "# #"],
    "o": ["###", "# #", "# #", "# #", "###"],
    "p": ["###", "# #", "###", "#  ", "#  "],
    "q": ["###", "# #", "###", "  #", "  #"],
    "r": ["###", "# #", "## ", "# #", "# #"],
    "s": ["###", "#  ", "###", "  #", "###"],
    "t": ["###", " # ", " # ", " # ", " # "],
    "u": ["# #", "# #", "# #", "# #", "###"],
    "v": ["# #", "# #", "# #", "# #", " # "],
    "w": ["# #", "# #", "# #", "###", "###"],
    "x": ["# #", " # ", " # ", " # ", "# #"],
    "y": ["# #", "# #", "###", "  #", "###"],
    "z": ["###", "  #", " # ", "#  ", "###"],
    " ": ["   ", "   ", "   ", "   ", "   "],
    "1": [" # ", "## ", " # ", " # ", "###"],
    "2": ["###", "  #", "###", "#  ", "###"],
    "3": ["###", "  #", "###", "  #", "###"],
    "4": ["# #", "# #", "###", "  #", "  #"],
    "5": ["###", "#  ", "###", "  #", "###"],
    "6": ["###", "#  ", "###", "# #", "###"],
    "7": ["###", "  #", "  #", " # ", "#  "],
    "8": ["###", "# #", "###", "# #", "###"],
    "9": ["###", "# #", "###", "  #", "###"],
    "0": ["###", "# #", "# #", "# #", "###"],
    "!": ["#", "#", "#", " ", "#"],
    "?": ["###", "  #", " # ", "   ", " # "],
    ".": [" ", " ", " ", " ", "#"],
    "[": ["##", "# ", "# ", "# ", "##"],
    "]": ["##", " #", " #", " #", "##"],
    "/": ["  #", "  #", " # ", " # ", "#  "],
    ":": [" ", "#", " ", "#", " "],
    "-": ["  ", "  ", "##", "  ", "  "],
    "'": ["#", "#", " ", " ", " "],
}


def gen_letters(text):
    bigletters = [LETTERS.get(i.lower(), LETTERS[" "]) for i in text]
    return "\n".join(["  ".join([b[l] for b in bigletters]) for l in range(5)])

def hours(countdown):
    return __hours_div_mod(countdown)[0]

def __hours_div_mod(countdown):
    return divmod(countdown.seconds, 3600)

def minutes(countdown):
    return divmod( __hours_div_mod(countdown)[1], 60)[0]

def seconds(countdown):
    return divmod( __hours_div_mod(countdown)[1], 60)[1]

def main():

    today = datetime.today()
    christmas = datetime(today.year, 12, 25)

    countdown = christmas - today

    hours_until = str(hours(countdown))
    minutes_until = str(minutes(countdown))
    seconds_until = str(seconds(countdown))

    print(gen_letters(hours_until + "-" + minutes_until + "-" + seconds_until))

    # print(gen_letters(str(countdown)))
#     print(
# """.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:..:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:
# .                                                                                           .
# .                                                                                           .
# .                                                                                           .
# .                                                                                           .
# .                                                                                           .
# .                                                                                           .
# .                                                                                           .
# .                                                                                           .
# .                                                                                           .
# .                                                                                           .
# .                                                                                           .
# .                                                                                           .
# .                                                                                           .
# .                                                                                           .
# .                                   |                         _...._                        .
# .                                \  _  /                    .::o:::::.                      .
# .                                 (\o/)                    .:::'''':o:.                     .
# .                             ---  / \  ---                :o:_    _:::                     .
# .                                  >*<                     `:}_>()<_{:'                     .
# .                                 >0<@<                 @    `'//\\\\'`    @                  .
# .                                >>>@<<*              @ #     //  \\\\     # @                .
# .                               >@>*<0<<<           __#_#____/'____'\____#_#__              .
# .                              >*>>@<<<@<<         [__________________________]             .
# .                             >@>>0<<<*<<@<         |=_- .-/\ /\ /\ /\--. =_-|              .
# .                            >*>>0<<@<<<@<<<        |-_= | \ \\\\ \\\\ \\\\ \ |-_=-|              .
# .                           >@>>*<<@<>*<<0<*<       |_=-=| / // // // / |_=-_|              .
# .             \*/          >0>>*<<@<>0><<*<@<<      |=_- |`-'`-'`-'`-'  |=_=-|              .
# .         ___/\\\\U//___    >*>>@><0<<*>>@><*<0<<     | =_-| o          o |_==_|              .
# .         |\\\\ | | \\\\|    >@>>0<*<<0>>@<<0<<<*<@<    |=_- | !     (    ! |=-_=|              .
# .         | \\\\| | _(UU)_ >((*))_>0><*<0><@<<<0<*<  _|-,-=| !    ).    ! |-_-=|_             .
# .         |\ \| || / //||.*.*.*.|>>@<<*<<@>><0<<@</=-((=_| ! __(:')__ ! |=_==_-\            .
# .         |\\\\_|_|&&_// ||*.*.*.*|_\\db//__     (\_/)-=))-|/^\=^=^^=^=/^\| _=-_-_\            .
# .         \"\"\"\"|\'.\'.\'|~~|.*.*.*|     ____|_   =(\'.\')=//   ,------------.                     .
# .             '.\'.\'.|   ^^^^^^|____|>>>>>>|  ( ~~~ )/   (((((((())))))))                    .
# .             ~~~~~~~~         \"\"\"\"\'------'  \'w---w\'     \'------------\'                     .
# .                                                                                           .
# .:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:.""")

if __name__ == '__main__':
    main()