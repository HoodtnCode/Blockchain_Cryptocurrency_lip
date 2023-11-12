
from encodings import utf_8
import hashlib
import json


#function to turn intergers into strings to input into encode function
#def stringafy(data):
#    return json.dumps(data)


#*args takes the place of data and allows to intake as many argumetns we wnat to pass into the method
def crypto_hash(*args):
    """
    Return a sha-256 hash of the given arguments.
    """
    #in order to take in stings and numbers python can put data(input) into json form at which turns into a string
    #endode method below only takes in strings and not intergers
    #stringafy_data = json.dumps(data)

    #since usign arguments not use map() function to ensure intergers can be hashed with encode
    #maps takes both a function and an argument function will be created outside of crypto_hash and string data
    #stringafy_args = map(stringafy , args)

    #use lambda for stringafy_args variable above for a single line code. that is becasue the stringafy funciton
    #is only created for the variable. lamda will take away functiont to single line
    stringafy_args = sorted(map(lambda data: json.dumps(data), args))

    #debug arguments
    #print(f'stringafy_args: {stringafy_args}') #debug
    
    joined_data = ''.join(stringafy_args)
    #print(f'joined_data: {joined_data}') #debug

    #encode o utf-8, if not an error will say the objects must be endoded before hashing into a byte string
    #before going into sha256 method. in a sting method to say take the data and convert to utf8 byte
    #turn to hex digest to a 64 character sting. encode only takes in strings and not intergers
    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()

def main():
    print (f"crypto_hash('one', 2 , [3]): {crypto_hash('one', 2, [3])}")
    print (f"crypto_hash(2,'one,' [3]): {crypto_hash( 2, 'one', [3])}") #use of sorted on stringafy ensures same hash output no matter the order


if __name__ == '__main__':
    main()