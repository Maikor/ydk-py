


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'MatchSetOptionsRestrictedType_Enum' : _MetaInfoEnum('MatchSetOptionsRestrictedType_Enum', 'ydk.models.policy.policy_types',
        {
            'ANY':'ANY',
            'INVERT':'INVERT',
        }, 'policy-types', _yang_ns._namespaces['policy-types']),
    'MatchSetOptionsType_Enum' : _MetaInfoEnum('MatchSetOptionsType_Enum', 'ydk.models.policy.policy_types',
        {
            'ANY':'ANY',
            'ALL':'ALL',
            'INVERT':'INVERT',
        }, 'policy-types', _yang_ns._namespaces['policy-types']),
    'AttributeComparison_Identity' : {
        'meta_info' : _MetaInfoClass('AttributeComparison_Identity',
            False, 
            [
            ],
            'policy-types',
            'attribute-comparison',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.policy.policy_types'
        ),
    },
    'InstallProtocolType_Identity' : {
        'meta_info' : _MetaInfoClass('InstallProtocolType_Identity',
            False, 
            [
            ],
            'policy-types',
            'install-protocol-type',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.policy.policy_types'
        ),
    },
    'AttributeEq_Identity' : {
        'meta_info' : _MetaInfoClass('AttributeEq_Identity',
            False, 
            [
            ],
            'policy-types',
            'attribute-eq',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.policy.policy_types'
        ),
    },
    'AttributeGe_Identity' : {
        'meta_info' : _MetaInfoClass('AttributeGe_Identity',
            False, 
            [
            ],
            'policy-types',
            'attribute-ge',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.policy.policy_types'
        ),
    },
    'AttributeLe_Identity' : {
        'meta_info' : _MetaInfoClass('AttributeLe_Identity',
            False, 
            [
            ],
            'policy-types',
            'attribute-le',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.policy.policy_types'
        ),
    },
    'BGP_Identity' : {
        'meta_info' : _MetaInfoClass('BGP_Identity',
            False, 
            [
            ],
            'policy-types',
            'BGP',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.policy.policy_types'
        ),
    },
    'DIRECTLYCONNECTED_Identity' : {
        'meta_info' : _MetaInfoClass('DIRECTLYCONNECTED_Identity',
            False, 
            [
            ],
            'policy-types',
            'DIRECTLY-CONNECTED',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.policy.policy_types'
        ),
    },
    'ISIS_Identity' : {
        'meta_info' : _MetaInfoClass('ISIS_Identity',
            False, 
            [
            ],
            'policy-types',
            'ISIS',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.policy.policy_types'
        ),
    },
    'LOCALAGGREGATE_Identity' : {
        'meta_info' : _MetaInfoClass('LOCALAGGREGATE_Identity',
            False, 
            [
            ],
            'policy-types',
            'LOCAL-AGGREGATE',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.policy.policy_types'
        ),
    },
    'OSPF3_Identity' : {
        'meta_info' : _MetaInfoClass('OSPF3_Identity',
            False, 
            [
            ],
            'policy-types',
            'OSPF3',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.policy.policy_types'
        ),
    },
    'OSPF_Identity' : {
        'meta_info' : _MetaInfoClass('OSPF_Identity',
            False, 
            [
            ],
            'policy-types',
            'OSPF',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.policy.policy_types'
        ),
    },
    'STATIC_Identity' : {
        'meta_info' : _MetaInfoClass('STATIC_Identity',
            False, 
            [
            ],
            'policy-types',
            'STATIC',
            _yang_ns._namespaces['policy-types'],
        'ydk.models.policy.policy_types'
        ),
    },
}