class Solution:
    def defangIPaddr(self, address: str) -> str:
        """
        Return a defanged IP address from a given IPv4 address.
        """
        defanged_address = address.replace('.', '[.]')
        return defanged_address
