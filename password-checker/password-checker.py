import requests
import hashlib
import sys

def main(argv):
    for password in argv:
        count = sha_converter(password)
        if count:
            print(f'{password} was found {count} times.... do change the password')
        else:
            print(f'{password} was not found\nyour password is strong')
    return 'All done'

x = int()

def requesting_api_data(_hash):
    url = 'https://api.pwnedpasswords.com/range/' + _hash
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError('There is problem in fetching the data\nplease check the password again')
    return res


def read_res(hashes, hash_to_check):
    hashes1 = (line.split(':')for line in hashes.text.splitlines())
    for hash, total in hashes1:
        if hash == hash_to_check:
            return total
    return 0


def sha_converter(password):
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    print(sha1_password)
    first5, tail = sha1_password[:5], sha1_password[5:]
    response = requesting_api_data(first5)
    return read_res(response, tail)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
