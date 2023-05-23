#===========================task2(worksheet2.1)===========================
import morse
import assert_tests

if __name__ == '__main__':
    e = morse.encode('us')
    print('%s' % e)
    d = morse.decode(e)
    print('\n')
    assert morse.encode('us') == '..- ...', "Should be ..- ..."
    assert morse.decode('..- ...') == 'US' , "Should be US"