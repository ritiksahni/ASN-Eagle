# ASN-Eagle
A tool to discover ASN of any host.

## Installation

1. Create an account on [Shodan](https://www.shodan.io/) and login.
2. After logging in, copy your shodan API key from [here](https://account.shodan.io/).
3. Enter the following commands.
```bash
git clone https://github.com/ritiksahni/ASN-Eagle.git
chmod +x setup.py
chmod +x ASN-Eagle.py
./setup.py install
```
4. Enter your Shodan API key.
5. Now, you're good to run ASN-Eagle :)


## Usage
```bash
./ASN-Eagle.py
```
Then, enter the hostname to search for its ASN (for e.g. google.com)

## Note:
Don't delete config.py after the setup, if it gets deleted please run ./setup.py install
