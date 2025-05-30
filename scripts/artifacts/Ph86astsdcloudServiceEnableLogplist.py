__artifacts_v2__ = {
    'Ph86assetsdcloudServiceEnableLogPlist': {
        'name': 'Ph86-assetsd-cloud-Service-Enable-Log-Plist',
        'description': 'Parses basic data from */PhotoData/private/com.apple.accountsd/cloudServiceEnableLog.plist'
                       ' which is a plist that tracks when Cloud Photos Library (CPL) has been enabled.'
                       ' Based on research and published blogs written by Scott Koenig https://theforensicscooter.com/',
        'author': 'Scott Koenig',
        'version': '5.0',
        'date': '2025-01-05',
        'requirements': 'Acquisition that contains assetsd cloudServiceEnableLog.plist',
        'category': 'Photos-Z-Settings',
        'notes': '',
        'paths': ('*/com.apple.assetsd/cloudServiceEnableLog.plist',),
        "output_types": ["standard", "tsv", "none"],
        "artifact_icon": "settings"
    }
}

import datetime
import os
import plistlib
import nska_deserialize as nd
from scripts.builds_ids import OS_build
from scripts.ilapfuncs import artifact_processor, logfunc, device_info, get_file_path

@artifact_processor
def Ph86assetsdcloudServiceEnableLogPlist(files_found, report_folder, seeker, wrap_text, timezone_offset):
    data_list = []
    source_path = str(files_found[0])

    with open(source_path, "rb") as fp:
        pl = plistlib.load(fp)
    if len(pl) > 0:
        for key in pl:
            if 'timestamp' in key:
                timestamputc = key['timestamp']
            else:
                timestamputc = ''
            if 'type' in key:
                servicetype = key['type']
            else:
                servicetype = ''
            if 'enabled' in key:
                enabledstate = key['enabled']
            else:
                enabledstate = ''

            data_list.append((timestamputc, servicetype, enabledstate))

    data_headers = (
        'TimestampUTC',
        'Service-Type',
        'Enabled-State')
    return data_headers, data_list, source_path
