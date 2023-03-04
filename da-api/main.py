from fastapi import FastAPI

app = FastAPI()

pet_data = [{
   	 "owner_id": 752833,
   	 "pet_id": 90608,
   	 "chip_id": 2684931842,
   	 "first_name": "Spot",
   	 "last_name": "Aguirre",
   	 "species": "dog",
   	 "breed": "dalmation",
   	 "age": 9,
   	 "weight": 64,
   	 "sex": "M"
    },
    {
   	 "owner_id": 602281,
   	 "pet_id": 39471,
   	 "chip_id": 4286286528,
   	 "first_name": "Mr. Bing",
   	 "last_name": "James",
   	 "species": "dog",
   	 "breed": "poodle",
   	 "age": 5,
   	 "weight": 59,
   	 "sex": "M"
    },
    {
   	 "owner_id": 365542,
   	 "pet_id": 48619,
   	 "chip_id": 6522709402,
   	 "first_name": "Buddy",
   	 "last_name": "Buckley",
   	 "species": "dog",
   	 "breed": "pitbull",
   	 "age": 4,
   	 "weight": 102,
   	 "sex": "F"
    },
    {
   	 "owner_id": 781523,
   	 "pet_id": 35851,
   	 "chip_id": 4749934929,
   	 "first_name": "Socks",
   	 "last_name": "Everett",
   	 "species": "cat",
   	 "breed": "calico",
   	 "age": 20,
   	 "weight": 12,
   	 "sex": "F"
    },
    {
   	 "owner_id": 837742,
   	 "pet_id": 70671,
   	 "chip_id": 6047761976,
   	 "first_name": "Max",
   	 "last_name": "Reid",
   	 "species": "dog",
   	 "breed": "pitbull",
   	 "age": 12,
   	 "weight": 65,
   	 "sex": "M"
    },
    {
   	 "owner_id": 837742,
   	 "pet_id": 46431,
   	 "chip_id": 2547744976,
   	 "first_name": "Alfred",
   	 "last_name": "Reid",
   	 "species": "dog",
   	 "breed": "german_shephard",
   	 "age": 8,
   	 "weight": 59,
   	 "sex": "M"
    },
    {
   	 "owner_id": 566256,
   	 "pet_id": 84471,
   	 "chip_id": 3518244576,
   	 "first_name": "Kitty",
   	 "last_name": "Santiago",
   	 "species": "cat",
   	 "breed": "tabby",
   	 "age": 4,
   	 "weight": 10,
   	 "sex": "F"
    },
    {
   	 "owner_id": 866118,
   	 "pet_id": 48775,
   	 "chip_id": 6237997004,
   	 "first_name": "Daisy",
   	 "last_name": "Norton",
   	 "species": "dog",
   	 "breed": "poodle",
   	 "age": 1,
   	 "weight": 35,
   	 "sex": "F"
    },
    {
   	 "owner_id": 284564,
   	 "pet_id": 98765,
   	 "chip_id": 1706228841,
   	 "first_name": "Sandy",
   	 "last_name": "Cervantes",
   	 "species": "dog",
   	 "breed": "labrador",
   	 "age": 3,
   	 "weight": 74,
   	 "sex": "F"
    },
    {
   	 "owner_id": 817092,
   	 "pet_id": 76543,
   	 "chip_id": 6827396840,
   	 "first_name": "Lola",
   	 "last_name": "Robles",
   	 "species": "cat",
   	 "breed": "persian",
   	 "age": 15,
   	 "weight": 10,
   	 "sex": "F"
    },
    {
   	 "owner_id": 899237,
   	 "pet_id": 43543,
   	 "chip_id": 4982736840,
   	 "first_name": "Kiki",
   	 "last_name": "Lane",
   	 "species": "cat",
   	 "breed": "maine_coon",
   	 "age": 5,
   	 "weight": 15,
   	 "sex": "F"
    },
    {
   	 "owner_id": 885604,
   	 "pet_id": 90876,
   	 "chip_id": 4379960296,
   	 "first_name": "Toby",
   	 "last_name": "Bowen",
   	 "species": "dog",
   	 "breed": "daschund",
   	 "age": 7,
   	 "weight": 28,
   	 "sex": "M"
    },
    {
   	 "owner_id": 674397,
   	 "pet_id": 80765,
   	 "chip_id": 6468550619,
   	 "first_name": "Fang",
   	 "last_name": "Galloway",
   	 "species": "dog",
   	 "breed": "husky",
   	 "age": 8,
   	 "weight": 57,
   	 "sex": "M"
    },
    {
   	 "owner_id": 864123,
   	 "pet_id": 77630,
   	 "chip_id": 6493437297,
   	 "first_name": "Whiskers",
   	 "last_name": "Garcia",
   	 "species": "cat",
   	 "breed": "siamese",
   	 "age": 2,
   	 "weight": 12,
   	 "sex": "F"
    },
    {
   	 "owner_id": 588863,
   	 "pet_id": 64319,
   	 "chip_id": 5196502091,
   	 "first_name": "Fluffy",
   	 "last_name": "Salinas",
   	 "species": "cat",
   	 "breed": "sphynx",
   	 "age": 10,
   	 "weight": 8,
   	 "sex": "F"
    },
    {
   	 "owner_id": 522709,
   	 "pet_id": 56720,
   	 "chip_id": 8769946197,
   	 "first_name": "Sammy",
   	 "last_name": "Greene",
   	 "species": "dog",
   	 "breed": "pug",
   	 "age": 3,
   	 "weight": 22,
   	 "sex": "M"
    },
    {
   	 "owner_id": 284564,
   	 "pet_id": 90672,
   	 "chip_id": 6177737992,
   	 "first_name": "Chloe",
   	 "last_name": "Cervantes",
   	 "species": "dog",
   	 "breed": "poodle",
   	 "age": 6,
   	 "weight": 36,
   	 "sex": "F"
    },
    {
   	 "owner_id": 837742,
   	 "pet_id": 84763,
   	 "chip_id": 6683530499,
   	 "first_name": "Mittens",
   	 "last_name": "Reid",
   	 "species": "cat",
   	 "breed": "bengal",
   	 "age": 11,
   	 "weight": 13,
   	 "sex": "F"
    },
    {
   	 "owner_id": 522709,
   	 "pet_id": 82763,
   	 "chip_id": 8683530499,
   	 "first_name": "Maxwell",
   	 "last_name": "Greene",
   	 "species": "cat",
   	 "breed": "persian",
   	 "age": 17,
   	 "weight": 12,
   	 "sex": "M"
    }
]

paymet_data = [{
   	 "owner_id": 752833,
   	 "payment_id": "461BE376-B450-4CAD-9CD1-7574F0244E0F",
   	 "staff_id": 3823,
   	 "payment_date": "Feb 24, 2022",
   	 "payment_amount": "$70.45"
    },
    {
   	 "owner_id": 602281,
   	 "payment_id": "05BD3BE9-6AB9-932B-E90E-8298D5753C20",
   	 "staff_id": 5612,
   	 "payment_date": "Mar 11, 2022",
   	 "payment_amount": "$38.83"
    },
    {
   	 "owner_id": 365542,
   	 "payment_id": "7A030183-3949-D8B7-E24B-80388FE970B6",
   	 "staff_id": 2873,
   	 "payment_date": "Feb 12, 2022",
   	 "payment_amount": "$233.81"
    },
    {
   	 "owner_id": 781523,
   	 "payment_id": "688769EC-41C2-44FD-0D9B-7335AEE222C6",
   	 "staff_id": 1133,
   	 "payment_date": "Feb 12, 2022",
   	 "payment_amount": "$115.92"
    },
    {
   	 "owner_id": 837742,
   	 "payment_id": "5B3B92DA-B1C4-E86A-2DA6-7F4D45D79EDD",
   	 "staff_id": 3823,
   	 "payment_date": "Jun 11, 2022",
   	 "payment_amount": "$147.78"
    },
    {
   	 "owner_id": 837742,
   	 "payment_id": "52527234-A88E-1E09-3EEB-57ABCD5946C1",
   	 "staff_id": 2873,
   	 "payment_date": "Jun 11, 2022",
   	 "payment_amount": "$87.78"
    },
    {
   	 "owner_id": 464301,
   	 "payment_id": "8F2A2D1A-3A3E-1F8F-7A39-A2A9D2DCB6A7",
   	 "staff_id": 1133,
   	 "payment_date": "Mar 16, 2022",
   	 "payment_amount": "$31.41"
    },
    {
   	 "owner_id": 566256,
   	 "payment_id": "B5F5B5D5-FBE8-2D2F-3F75-9D3CF56F59D5",
   	 "staff_id": 5612,
   	 "payment_date": "Jun 12, 2022",
   	 "payment_amount": "$90.41"
    },
    {
   	 "owner_id": 866118,
   	 "payment_id": "280A4F1F-7B4F-A4C6-A0E9-A6AF2D6B2FA2",
   	 "staff_id": 1133,
   	 "payment_date": "Jun 11, 2022",
   	 "payment_amount": "$87.41"
    },
    {
   	 "owner_id": 284564,
   	 "payment_id": "6B324BD7-E57A-F73D-C41B-34D0547C2B2C",
   	 "staff_id": 2873,
   	 "payment_date": "Jun 24, 2022",
   	 "payment_amount": "$76.59"
    },
    {
   	 "owner_id": 817092,
   	 "payment_id": "EC90C8F3-A5B9-1C9F-F8D8-C7CD2C2B2C2E",
   	 "staff_id": 5612,
   	 "payment_date": "Feb 24, 2022",
   	 "payment_amount": "$73.91"
    },
    {
   	 "owner_id": 899237,
   	 "payment_id": "8B3C7F2F-A9A9-90A8-1D26-1F1C25E75A68",
   	 "staff_id": 1133,
   	 "payment_date": "Mar 23, 2022",
   	 "payment_amount": "$32.63"
    },
    {
   	 "owner_id": 885604,
   	 "payment_id": "C70DFFDE-6439-9D44-8A13-F7D18A2F2EDE",
   	 "staff_id": 2873,
   	 "payment_date": "Mar 18, 2022",
   	 "payment_amount": "$125.62"
    },
    {
   	 "owner_id": 674397,
   	 "payment_id": "5F5A7B17-6A4E-D922-0FD4-30D4E3A3D0E3",
   	 "staff_id": 1133,
   	 "payment_date": "Jun 16, 2022",
   	 "payment_amount": "$139.95"
    },
    {
   	 "owner_id": 864123,
   	 "payment_id": "0C8F19DD-D9A3-3E90-DDE2-B2D18EFD5CA5",
   	 "staff_id": 5612,
   	 "payment_date": "Jun 25, 2022",
   	 "payment_amount": "$90.24"
    },
    {
   	 "owner_id": 588863,
   	 "payment_id": "F7C6B8A7-9EE2-0621-7D0F-8C439E7FBCF1",
   	 "staff_id": 2873,
   	 "payment_date": "Mar 11, 2022",
   	 "payment_amount": "$176.78"
    },
    {
   	 "owner_id": 522709,
   	 "payment_id": "7D00FA63-1A7C-EF64-E7AF-BBD8F53D7E32",
   	 "staff_id": 1133,
   	 "payment_date": "Mar 18, 2022",
   	 "payment_amount": "$41.28"
    },
    {
   	 "owner_id": 899237,
   	 "payment_id": "0EA0FBB7-B8F9-F7F2-2EF1-7DA592F8E7D7",
   	 "staff_id": 5612,
   	 "payment_date": "Feb 12, 2022",
   	 "payment_amount": "$126.17"
    },
    {
   	 "owner_id": 464301,
   	 "payment_id": "3F2D7F2F-2A9D-E2B2-0BFC-48F78C7E00C0",
   	 "staff_id": 2873,
   	 "payment_date": "Feb 26, 2022",
   	 "payment_amount": "$12.14"
    },
    {
   	 "owner_id": 365542,
   	 "payment_id": "B3A7A1F8-FAAE-D2F7-0FFC-D8808FAF9DFC",
   	 "staff_id": 1133,
   	 "payment_date": "Jun 25, 2022",
   	 "payment_amount": "$73.34"
    },
    {
   	 "owner_id": 522709,
   	 "payment_id": "2030A4A8-C7A7-6B0B-F37C-8D73F9A9A1E9",
   	 "staff_id": 5612,
   	 "payment_date": "Feb 26, 2022",
   	 "payment_amount": "$84.24"
    }
]

owner_data = [{
   	 "owner_id": 752833,
   	 "first_name": "Erica",
   	 "last_name": "Aguirre",
   	 "phone": "1-836-728-6635",
   	 "email": "christopherholmes@protonmail.com",
   	 "address": "4721 Sit Ave",
   	 "city": "Flint",
   	 "zip_code": "76485"
    },
    {
   	 "owner_id": 602281,
   	 "first_name": "Griffith",
   	 "last_name": "James",
   	 "phone": "(869) 597-3357",
   	 "email": "jeremycooper@aol.edu",
   	 "address": "501-2173 Aenean Rd.",
   	 "city": "Georgia",
   	 "zip_code": "36763"
    },
    {
   	 "owner_id": 365542,
   	 "first_name": "Faith",
   	 "last_name": "Buckley",
   	 "phone": "1-642-832-2264",
   	 "email": "ravenbrooks1943@hotmail.ca",
   	 "address": "Ap #280-4855 Lorem, Road",
   	 "city": "Saint Louis",
   	 "zip_code": "56355"
    },
    {
   	 "owner_id": 781523,
   	 "first_name": "Joseph",
   	 "last_name": "Everett",
   	 "phone": "1-794-116-5647",
   	 "email": "austinholden@aol.net",
   	 "address": "167-4873 Nisi Rd.",
   	 "city": "Minneapolis",
   	 "zip_code": "93447"
    },
    {
   	 "owner_id": 837742,
   	 "first_name": "Fiona",
   	 "last_name": "Reid",
   	 "phone": "1-463-433-5021",
   	 "email": "heddahunt@icloud.com",
   	 "address": "Ap #322-7223 Lectus. St.",
   	 "city": "Broken Arrow",
   	 "zip_code": "23663"
    },
    {
   	 "owner_id": 464301,
   	 "first_name": "Vance",
   	 "last_name": "Chen",
   	 "phone": "1-611-854-8275",
   	 "email": "edwardrichardson@protonmail.net",
   	 "address": "P.O. Box 690, 5489 Donec Rd.",
   	 "city": "Boston",
   	 "zip_code": "92805"
    },
    {
   	 "owner_id": 566256,
   	 "first_name": "Ryleigh",
   	 "last_name": "Santiago",
   	 "phone": "839-919-4392",
   	 "email": "hunterharvey@outlook.edu",
   	 "address": "297-6117 Vulputate, Rd.",
   	 "city": "Cheyenne",
   	 "zip_code": "73011"
    },
    {
   	 "owner_id": 866118,
   	 "first_name": "Tara",
   	 "last_name": "Norton",
   	 "phone": "1-848-219-4336",
   	 "email": "jennymorales@yahoo.com",
   	 "address": "Ap #943-3737 Arcu. Rd.",
   	 "city": "Reno",
   	 "zip_code": "74477"
    },
    {
   	 "owner_id": 284564,
   	 "first_name": "Alyson",
   	 "last_name": "Cervantes",
   	 "phone": "1-913-764-7975",
   	 "email": "alexanderdavies@aol.net",
   	 "address": "P.O. Box 552, 8529 In, Ave",
   	 "city": "Tampa",
   	 "zip_code": "91947"
    },
    {
   	 "owner_id": 817092,
   	 "first_name": "Dennis",
   	 "last_name": "Robles",
   	 "phone": "1-728-467-2915",
   	 "email": "brookehudson@yahoo.ca",
   	 "address": "Ap #475-2037 Nibh Rd.",
   	 "city": "Memphis",
   	 "zip_code": "79375"
    },
    {
   	 "owner_id": 899237,
   	 "first_name": "Yasmin",
   	 "last_name": "Lane",
   	 "phone": "1-872-819-1762",
   	 "email": "ethanmccarthy@hotmail.net",
   	 "address": "P.O. Box 699, 4244 Lorem St.",
   	 "city": "San Antonio",
   	 "zip_code": "63979"
    },
    {
   	 "owner_id": 885604,
   	 "first_name": "Jaden",
   	 "last_name": "Bowen",
   	 "phone": "1-686-738-8376",
   	 "email": "samanthaking@yahoo.ca",
   	 "address": "Ap #620-4115 Nec Street",
   	 "city": "Lansing",
   	 "zip_code": "19272"
    },
    {
   	 "owner_id": 674397,
   	 "first_name": "Rylee",
   	 "last_name": "Galloway",
   	 "phone": "1-649-732-3103",
   	 "email": "derekjames@outlook.com",
   	 "address": "Ap #716-6603 In Rd.",
   	 "city": "Oakland",
   	 "zip_code": "86152"
    },
    {
   	 "owner_id": 864123,
   	 "first_name": "Drake",
   	 "last_name": "Garcia",
   	 "phone": "1-280-855-4376",
   	 "email": "lillianspencer@hotmail.ca",
   	 "address": "P.O. Box 851, 6205 Tortor Rd.",
   	 "city": "Toledo",
   	 "zip_code": "54236"
    },
    {
   	 "owner_id": 588863,
   	 "first_name": "Amy",
   	 "last_name": "Salinas",
   	 "phone": "1-638-764-6827",
   	 "email": "braydencooper@outlook.edu",
   	 "address": "P.O. Box 683, 6653 Mauris Ave",
   	 "city": "Portland",
   	 "zip_code": "73272"
    },
    {
   	 "owner_id": 522709,
   	 "first_name": "Lilliana",
   	 "last_name": "Greene",
   	 "phone": "1-858-541-3986",
   	 "email": "josephroberts@icloud.net",
   	 "address": "Ap #917-9482 Tellus Rd.",
   	 "city": "Baton Rouge",
   	 "zip_code": "16425"
    }
]



@app.get("/pet")
def pets():
    return {'pet_data': pet_data}

@app.get("/payment")
def payments():
    return {'payment_data': paymet_data}


@app.get("/owner")
def owner():
    return {'owner_data': owner_data}