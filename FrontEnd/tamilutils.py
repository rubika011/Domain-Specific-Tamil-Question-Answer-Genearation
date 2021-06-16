import tamil

def getUnicodePoints(letter):
    try:
        # when uyir letters are passed it will throw an IndexError
        uyir_letters = tamil.utf8.uyir_letters
        rval = tamil.utf8.splitMeiUyir(letter)
        if not isinstance(rval, tuple):
            if rval in uyir_letters:
                print("This is an uyir letter")
                return (u'', rval)
            print(rval)
            return (rval, u'')
        print("Valid")
        print(rval)
        return rval
    except IndexError as idxerr:
        pass
    except ValueError as valerr:
        # non tamil letters cannot be split - e.g. '26வது'
        pass
        # could be english string etc. multiple-letter (word-like) input etc

    return (u'', u'')
