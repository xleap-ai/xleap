# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xleap._client.models.org_member import OrgMember


class TestOrgMember(unittest.TestCase):
    """OrgMember unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrgMember:
        """Test OrgMember
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `OrgMember`
        """
        model = OrgMember()
        if include_optional:
            return OrgMember(
                id = 56,
                username = '',
                first_name = '',
                last_name = '',
                email = ''
            )
        else:
            return OrgMember(
                username = '',
        )
        """

    def testOrgMember(self):
        """Test OrgMember"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
