# -*- coding: utf-8 -*-
#
# This file is part of EventGhost.
# Copyright © 2005-2016 EventGhost Project <http://www.eventghost.net/>
#
# EventGhost is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 2 of the License, or (at your option)
# any later version.
#
# EventGhost is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along
# with EventGhost. If not, see <http://www.gnu.org/licenses/>.

import ctypes
import comtypes
from .iid import IID_IAudioEndpointFormatControl
from ctypes.wintypes import (
    DWORD,
)

COMMETHOD = comtypes.COMMETHOD
HRESULT = ctypes.HRESULT
POINTER = ctypes.POINTER


class IAudioEndpointFormatControl(comtypes.IUnknown):
    _case_insensitive_ = True
    _iid_ = IID_IAudioEndpointFormatControl
    _methods_ = (
        COMMETHOD(
            [],
            HRESULT,
            'ResetToDefault',
            (['in'], DWORD, 'ResetFlags')
        ),
    )


PIAudioEndpointFormatControl = POINTER(IAudioEndpointFormatControl)

