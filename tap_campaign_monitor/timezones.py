import pytz


mapping = {
    "(GMT) Coordinated Universal Time": "GMT",
    "(GMT+00:00) Casablanca": "Africa/Casablanca",
    "(GMT+00:00) Dublin, Edinburgh, Lisbon, London": "Europe/Dublin",
    "(GMT+00:00) Monrovia, Reykjavik": "Atlantic/Reykjavik",
    "(GMT+01:00) Amsterdam, Berlin, Bern, Rome, Stockholm, Vienna": "Europe/Amsterdam",
    "(GMT+01:00) Belgrade, Bratislava, Budapest, Ljubljana, Prague": "Europe/Belgrade",
    "(GMT+01:00) Brussels, Copenhagen, Madrid, Paris": "Europe/Brussels",
    "(GMT+01:00) Sarajevo, Skopje, Warsaw, Zagreb": "Europe/Sarajevo",
    "(GMT+01:00) West Central Africa"
    "(GMT+02:00) Amman": "Asia/Amman",
    "(GMT+02:00) Athens, Bucharest": "Europe/Athens",
    "(GMT+02:00) Beirut": "Asia/Beirut",
    "(GMT+02:00) Cairo": "Africa/Cairo",
    "(GMT+02:00) Chisinau": "Europe/Chisinau",
    "(GMT+02:00) Damascus": "Asia/Damascus",
    "(GMT+02:00) Harare, Pretoria": "Africa/Harare",
    "(GMT+02:00) Helsinki, Kyiv, Riga, Sofia, Tallinn, Vilnius": "Europe/Helsinki",
    "(GMT+02:00) Jerusalem": "Asia/Jerusalem",
    "(GMT+02:00) Kaliningrad": "Europe/Kaliningrad",
    "(GMT+02:00) Tripoli": "Africa/Tripoli",
    "(GMT+03:00) Baghdad": "Asia/Baghdad",
    "(GMT+03:00) Istanbul": "Asia/Istanbul",
    "(GMT+03:00) Kuwait, Riyadh": "Asia/Kuwait",
    "(GMT+03:00) Minsk": "Europe/Minsk",
    "(GMT+03:00) Moscow, St. Petersburg, Volgograd": "Europe/Moscow",
    "(GMT+03:00) Nairobi": "Africa/Nairobi",
    "(GMT+03:30) Tehran": "Asia/Tehran",
    "(GMT+04:00) Abu Dhabi, Muscat": "Asia/Muscat",
    "(GMT+04:00) Baku": "Asia/Baku",
    "(GMT+04:00) Izhevsk, Samara": "Europe/Samara",
    "(GMT+04:00) Port Louis": "Indian/Mauritius",
    "(GMT+04:00) Tbilisi": "Asia/Tbilisi",
    "(GMT+04:00) Yerevan": "Asia/Yerevan",
    "(GMT+04:30) Kabul": "Asia/Kabul",
    "(GMT+05:00) Ashgabat, Tashkent": "Asia/Ashgabat",
    "(GMT+05:00) Ekaterinburg": "Asia/Yekaterinburg",
    "(GMT+05:00) Islamabad, Karachi": "Asia/Karachi",
    "(GMT+05:30) Chennai, Kolkata, Mumbai, New Delhi": "Asia/Kolkata",
    "(GMT+05:45) Kathmandu": "Asia/Kathmandu",
    "(GMT+06:00) Dhaka": "Asia/Dhaka",
    "(GMT+06:30) Yangon (Rangoon)": "Asia/Yangon",
    "(GMT+07:00) Bangkok, Hanoi, Jakarta": "Asia/Bangkok",
    "(GMT+07:00) Krasnoyarsk": "Asia/Krasnoyarsk",
    "(GMT+07:00) Novosibirsk": "Asia/Novosibirsk",
    "(GMT+08:00) Beijing, Chongqing, Hong Kong, Urumqi": "Asia/Chongqing",
    "(GMT+08:00) Irkutsk": "Asia/Irkutsk",
    "(GMT+08:00) Kuala Lumpur, Singapore": "Asia/Kuala_Lumpur",
    "(GMT+08:00) Perth": "Australia/Perth",
    "(GMT+08:00) Taipei": "Asia/Taipei",
    "(GMT+08:00) Ulaanbaatar": "Asia/Ulaanbaatar",
    "(GMT+09:00) Osaka, Sapporo, Tokyo": "Asia/Tokyo",
    "(GMT+09:00) Seoul": "Asia/Seoul",
    "(GMT+09:00) Yakutsk": "Asia/Yakutsk",
    "(GMT+09:30) Adelaide": "Australia/Adelaide",
    "(GMT+09:30) Darwin": "Australia/Darwin",
    "(GMT+10:00) Brisbane": "Australia/Brisbane",
    "(GMT+10:00) Canberra, Melbourne, Sydney": "Australia/Canberra",
    "(GMT+10:00) Guam, Port Moresby": "Pacific/Guam",
    "(GMT+10:00) Hobart": "Australia/Hobart",
    "(GMT+10:00) Vladivostok": "Asia/Vladivostok",
    "(GMT+11:00) Bougainville Island": "Pacific/Bougainville",
    "(GMT+11:00) Magadan": "Asia/Magadan",
    "(GMT+11:00) Solomon Is., New Caledonia"
    "(GMT+12:00) Anadyr, Petropavlovsk-Kamchatsky": "Asia/Anadyr",
    "(GMT+12:00) Auckland, Wellington": "Pacific/Auckland",
    "(GMT+12:00) Coordinated Universal Time+12": "Etc/GMT+12",
    "(GMT+12:00) Fiji": "Pacific/Fiji",
    "(GMT+13:00) Samoa": "Pacific/Samoa",
    "(GMT+14:00) Kiritimati Island": "Pacific/Kiritimati",
    "(GMT-01:00) Azores": "Atlantic/Azores",
    "(GMT-01:00) Cabo Verde Is.": "Atlantic/Cape_Verde",
    "(GMT-02:00) Coordinated Universal Time-02": "Etc/GMT-2",
    "(GMT-03:00) Araguaina": "America/Araguaina",
    "(GMT-03:00) Brasilia": "Brazil/East",
    "(GMT-03:00) Cayenne, Fortaleza": "America/Cayenne",
    "(GMT-03:00) City of Buenos Aires": "America/Argentina/Buenos_Aires",
    "(GMT-03:00) Montevideo": "America/Montevideo",
    "(GMT-03:00) Salvador": "America/El_Salvador",
    "(GMT-03:30) Newfoundland": "Canada/Newfoundland",
    "(GMT-04:00) Asuncion": "America/Asuncion",
    "(GMT-04:00) Atlantic Time (Canada)": "Canada/Atlantic",
    "(GMT-04:00) Caracas": "America/Caracas",
    "(GMT-04:00) Cuiaba": "America/Cuiaba",
    "(GMT-04:00) Georgetown, La Paz, Manaus, San Juan": "America/La_Paz",
    "(GMT-04:00) Santiago": "America/Santiago",
    "(GMT-05:00) Bogota, Lima, Quito, Rio Branco": "America/Bogota",
    "(GMT-05:00) Eastern Time (US & Canada)": "US/Eastern",
    "(GMT-06:00) Central Time (US & Canada)": "US/Central",
    "(GMT-06:00) Guadalajara, Mexico City, Monterrey": "America/Mexico_City",
    "(GMT-06:00) Saskatchewan": "Canada/Saskatchewan",
    "(GMT-07:00) Arizona": "US/Arizona",
    "(GMT-07:00) Chihuahua, La Paz, Mazatlan": "America/Chihuahua",
    "(GMT-07:00) Mountain Time (US & Canada)": "US/Mountain",
    "(GMT-08:00) Baja California": "Mexico/BajaNorte",
    "(GMT-08:00) Pacific Time (US & Canada)": "US/Pacific",
    "(GMT-09:00) Alaska": "US/Alaska",
    "(GMT-10:00) Hawaii": "US/Hawaii",
    "(GMT-11:00) Coordinated Universal Time-11": "Etc/GMT-11",
    "(GMT-12:00) International Date Line West": "Etc/GMT-12",
}


def from_string(s):
    if mapping.get(s) is None:
        return None

    return pytz.timezone(mapping.get(s))