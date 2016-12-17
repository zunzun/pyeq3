
#    pyeq3 is a collection of equations expressed as Python classes
#
#    Copyright (C) 2013 James R. Phillips
#    2548 Vera Cruz Drive
#    Birmingham, AL 35235 USA
#
#    email: zunzun@zunzun.com
#
#    License: BSD-style (see LICENSE.txt in main source directory)

import sys
ver = sys.version_info[0]
if ver < 3:
    raise Exception('Python 3 is required to use pyeq3')

from . import DataCache
from . import Services
from . import ExtendedVersionHandlers
from . import IModel
from . import Models_2D
from . import Models_3D

dataConvertorService = Services.DataConverterService.DataConverterService
solverService = Services.SolverService.SolverService
outputSourceCodeService = Services.OutputSourceCodeService.OutputSourceCodeService
dataCache = DataCache.DataCache.DataCache
