from datetime import date

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

def hours_to(countdown):
    return str(divmod(countdown.total_seconds(), 3600))

def minutes_to(countdown):
    return str(divmod(countdown.total_seconds(), 60))


def getDuration(then, now=date.today(), interval="default"):
    # Returns a duration as specified by variable interval
    # Functions, except totalDuration, returns [quotient, remainder]

    duration = now - then  # For build-in functions
    duration_in_s = duration.total_seconds()

    def years():
        return divmod(duration_in_s, 31536000)  # Seconds in a year=31536000.

    def days(seconds=None):
        return divmod(seconds if seconds != None else duration_in_s, 86400)  # Seconds in a day = 86400

    def hours(seconds=None):
        return divmod(seconds if seconds != None else duration_in_s, 3600)  # Seconds in an hour = 3600

    def minutes(seconds=None):
        return divmod(seconds if seconds != None else duration_in_s, 60)  # Seconds in a minute = 60

    def seconds(seconds=None):
        if seconds != None:
            return divmod(seconds, 1)
        return duration_in_s

    def totalDuration():
        y = years()
        d = days(y[1])  # Use remainder to calculate next variable
        h = hours(d[1])
        m = minutes(h[1])
        s = seconds(m[1])

        return "Time between dates: {} years, {} days, {} hours, {} minutes and {} seconds".format(int(y[0]), int(d[0]),
                                                                                                   int(h[0]), int(m[0]),
                                                                                                   int(s[0]))

    return {
        'years': int(years()[0]),
        'days': int(days()[0]),
        'hours': int(hours()[0]),
        'minutes': int(minutes()[0]),
        'seconds': int(seconds()),
        'default': totalDuration()
    }[interval]





def main():

    today = date.today()
    christmas = date(today.year, 12, 25)

    countdown = christmas - today

    print(countdown)


    hours = hours_to(countdown)
    mins = minutes_to(countdown)

    # Example usage
    # then = date(2012, 3, 5, 23, 8, 15)
    # now = date.today()
    #
    # print(getDuration(then))  # E.g. Time between dates: 7 years, 208 days, 21 hours, 19 minutes and 15 seconds
    # print(getDuration(then, now, 'years'))  # Prints duration in years
    # print(getDuration(then, now, 'days'))  # days
    # print(getDuration(then, now, 'hours'))  # hours
    # print(getDuration(then, now, 'minutes'))  # minutes
    # print(getDuration(then, now, 'seconds'))  #


    until_christmas = gen_letters(str(countdown.days))
    until_christmas = gen_letters(hours)
    until_christmas = gen_letters(mins)
    until_christmas = gen_letters(str(countdown.total_seconds()))

    print(until_christmas)
    print(
""".:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:..:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:
.                                                                                           .
.                                                                                           .
.                                                                                           .
.                                                                                           .
.                                                                                           .
.                                                                                           .
.                                                                                           .
.                                                                                           .
.                                                                                           .
.                                                                                           .
.                                                                                           .
.                                                                                           .
.                                                                                           .
.                                                                                           .
.                                   |                         _...._                        .
.                                \  _  /                    .::o:::::.                      .
.                                 (\o/)                    .:::'''':o:.                     .
.                             ---  / \  ---                :o:_    _:::                     .
.                                  >*<                     `:}_>()<_{:'                     .
.                                 >0<@<                 @    `'//\\\\'`    @                  .
.                                >>>@<<*              @ #     //  \\\\     # @                .
.                               >@>*<0<<<           __#_#____/'____'\____#_#__              .
.                              >*>>@<<<@<<         [__________________________]             .
.                             >@>>0<<<*<<@<         |=_- .-/\ /\ /\ /\--. =_-|              .
.                            >*>>0<<@<<<@<<<        |-_= | \ \\\\ \\\\ \\\\ \ |-_=-|              .
.                           >@>>*<<@<>*<<0<*<       |_=-=| / // // // / |_=-_|              .
.             \*/          >0>>*<<@<>0><<*<@<<      |=_- |`-'`-'`-'`-'  |=_=-|              .
.         ___/\\\\U//___    >*>>@><0<<*>>@><*<0<<     | =_-| o          o |_==_|              .
.         |\\\\ | | \\\\|    >@>>0<*<<0>>@<<0<<<*<@<    |=_- | !     (    ! |=-_=|              .
.         | \\\\| | _(UU)_ >((*))_>0><*<0><@<<<0<*<  _|-,-=| !    ).    ! |-_-=|_             .
.         |\ \| || / //||.*.*.*.|>>@<<*<<@>><0<<@</=-((=_| ! __(:')__ ! |=_==_-\            .
.         |\\\\_|_|&&_// ||*.*.*.*|_\\db//__     (\_/)-=))-|/^\=^=^^=^=/^\| _=-_-_\            .
.         \"\"\"\"|\'.\'.\'|~~|.*.*.*|     ____|_   =(\'.\')=//   ,------------.                     .
.             '.\'.\'.|   ^^^^^^|____|>>>>>>|  ( ~~~ )/   (((((((())))))))                    .
.             ~~~~~~~~         \"\"\"\"\'------'  \'w---w\'     \'------------\'                     .
.                                                                                           .
.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:.""")

if __name__ == '__main__':
    main()