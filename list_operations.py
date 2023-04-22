empty_list = []
second_list = ["plate","spoon","chair","table","bag"]
print(len(second_list))
print(second_list[0],second_list[2],second_list[4])
mixed_data_type = ["Muhammed",23,5.9,"dating","Gaa Odota Community"]
it_companies = ["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
print(mixed_data_type)
print(it_companies)
print(len(it_companies))
print(it_companies[0],it_companies[3],it_companies[6])
it_companies[2] = "Twitter"
print(it_companies)
it_companies.append("Oppo")
it_companies.insert(3,"Samsung")
print(it_companies)
it_companies[0] = it_companies[0].upper()
print(it_companies)
print("#".join(it_companies))
print("Twitter" in it_companies)
it_companies.sort()
print(it_companies)
it_companies.sort(reverse=True)
print(it_companies)
first_3 = it_companies[0:3]
print(first_3)
middle_3 = it_companies[3:5]
print(middle_3)
last_ = it_companies[6:]
print(last_)
it_companies.remove("Twitter")
print(it_companies)
it_companies.remove("Google")
print(it_companies)
it_companies.pop(6)
print(it_companies)
it_companies.clear()
print(it_companies)
front_end = ["HTML","CSS","JS","React","Redux"]
back_end = ["Node","Express","MongoDB"]
full_stack = front_end + back_end
print(full_stack)
full_stack.insert(5,"Python")
full_stack.insert(6,"SQL")
print(full_stack)
ages = [19,22,19,24,20,25,26,24,25,24]
print(len(ages))
ages.sort()
print(ages)
min_ages = min(ages)
max_ages = max(ages)
print(min_ages,max_ages)
ages.append(min_ages)
ages.append(max_ages)
print(ages)
print(len(ages))
median_ages = ages[5]+ages[6]/2
print(f"Median age is {median_ages}")
mean_ages = sum(ages)/len(ages)
print(f"Mean age is {mean_ages}")
age_range = max_ages - min_ages
print(f"Age range is {age_range}")
comparison_value_a = (min_ages- mean_ages)
comparison_value_b = (max_ages - mean_ages)
print(comparison_value_a)
print(comparison_value_b)
print(abs(comparison_value_a),abs(comparison_value_b))
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
print(len(countries))
first_half_countries = countries[0:96]
second_half_countries = countries[96:]
print(first_half_countries)
print(second_half_countries)
print(len(first_half_countries))
print(len(second_half_countries))
first_country,second_country,third_country, *rest = ["China","Russia","USA","Finland","Sweden","Norway","Denmark"]
print(first_country)
print(second_country)
print(third_country)
Scandic_Countries = rest
print(Scandic_Countries)
