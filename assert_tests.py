#===========================task3(worksheet2.1)===========================
import morse

def test_encode_us():
    assert morse.encode('US') != '..- ...', "Should be..- .."

if __name__ == "__main__":
    test_encode_us()
    print('Everything passed')
