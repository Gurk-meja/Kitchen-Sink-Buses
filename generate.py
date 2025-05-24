import grf, lib
from datetime import date

g = lib.NewGRF(
    grfid="MEJA", # change
    name="Epic bus grf",
    description="An epic bus grf in grf-py",
    min_compatible_version=0,
    version=0, #should be 1 on release, 0 for testing
    id_map_file='id_map.json',
)

# roadtype table
(
    off_road,
    off_road_bus,
    all_terrain,
    all_terrain_bus,
    highway,
    highway_bus,
) = g.set_roadtype_table([
    ('RAAN', 'ROAD'),         # Off-road
    ('PAAN', 'RAAN', 'ROAD'), # Off-road Bus
    ('RABN', 'ROAD'),         # All terrain
    ('PABN', 'RABN', 'ROAD'), # All terrain Bus
    ('RACN', 'ROAD'),         # Highway only             
    ('PACN', 'RACN', 'ROAD'), # Highway only bus
])

#There are 5 different road terrains only A, B and C may be used
#Off-road only (a)
#Off-road and all-terrain (A)
#Off-road, all-terrain and highway (B)
#All-terrain and highway (C)
#Highway only (c) #doesn't exist as grf unsure about irl

#The bus types (P) are allowed on bus exclusive roads others (R) are not. 

RoadVehicle = g.bind(lib.RoadVehicle)

def tmpl_bus(func):
    return [
        func(  0, 8, 10, 44, xofs=-4,  yofs=-21),
        func( 20, 8, 42, 44, xofs=-24, yofs=-30),
        func( 70, 8, 69, 44, xofs=-34, yofs=-38),
        func(150, 8, 42, 44, xofs=-16, yofs=-30),
        func(200, 8, 10, 44, xofs=-4,  yofs=-21),
        func(220, 8, 42, 44, xofs=-24, yofs=-30),
        func(270, 8, 69, 44, xofs=-34, yofs=-38),
        func(350, 8, 42, 44, xofs=-16, yofs=-30),
    ]

Livery = lib.LiveryFactory(tmpl_bus)
paint_palette = lib.read_palette_file('compal.png')
PSDLivery = lambda *args, **kw: lib.PSDLivery(tmpl_bus, paint_palette, *args, **kw)

palette = lib.read_palette_file('compal.png')
colours = {
    
"MAGENTA" : palette[16: 24],
"PINK" : palette[24: 32],
"RED" : palette[32: 40],
"MAROON" : palette[40: 48],
"ORANGE" : palette[48: 56],
"BROWN" : palette[56: 64],
"REDBROWN" : palette[64: 72],
"YELLOWBROWN" : palette[72: 80],
"DCREAM" : palette[80: 88],
"CREAM" : palette[88: 96],
"YELLOW" : palette[96: 104],
"LIME" : palette[104: 112],
"GREEN" : palette[112: 120],
"DGREEN" : palette[120: 128],
"TURQUOISE" : palette[128: 136],
"DTURQUOISE" : palette[136: 144],
"SKY" : palette[144: 152],
"BLUE" : palette[152: 160],
"DBLUE" : palette[160: 168],
"COLBALT" : palette[168: 176],
"MAUVE" : palette[176: 184],
"LAVENDER" : palette[184: 192],
"PURPLE" : palette[192: 200],
"DPURPLE" : palette[200: 208],
"GREY1" : palette[232: 240],
"GREY2" : palette[240: 248],
"GREY3" : palette[248: 256],
"GREY4" : palette[256: 264],
"GREY5" : palette[264: 272],
"GREY6" : palette[272: 280],
"GREY7" : palette[280: 288],
"GREY8" : palette[288: 296],
"GREY9" : palette[296: 304],
"GREY10" : palette[304: 312],
"SEBROWN" : palette[344: 352],
"SCARLET" : palette[352: 360],
"SLBLUE" : palette[360: 368],
}

def make_psd_cc_liveries(psd_file, *, shading=None, paint=None, overlay=None, cc_replace, cc2_replace):
    return {
        'Default': PSDLivery(
            psd_file,
            shading=shading,
            paint=paint,
            overlay=overlay,
            cc_replace=cc_replace,
            cc2_replace=cc2_replace,
        ),
        '2CC': PSDLivery(
            psd_file,
            shading=shading,
            paint=paint,
            overlay=overlay,
            auto_cc=lib.CC_DEFAULT,
        ),
        '2CC alt': PSDLivery(
            psd_file,
            shading=shading,
            paint=paint,
            overlay=overlay,
            auto_cc=lib.CC_SWAPPED,
        ),
    }


COMMON_C1_PROPS = dict(
    length=8 ,
    misc_flags=RoadVehicle.Flags.USE_2CC,
    power_type='3rd',
    max_speed=RoadVehicle.kmhish(80),
    power=43,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=30,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=152,
    loading_speed=40,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    country='sweden',
)

verymuchabusnotatrain = RoadVehicle(
    **COMMON_C1_PROPS,
    id='s_e_C1_1',
    name='Off-road',
    liveries=make_psd_cc_liveries(
        'pp/1949_SE_C1.psd',
        shading='C1',
        paint='SS',
        overlay=('Lights',),
        cc_replace=colours["GREEN"],
        cc2_replace=colours["GREEN"]
    ),
    company='ss',
    road_type=off_road_bus,
    introduction_date=date(1949, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'SS/SL',
        'Use': 'Sockholm Metro buses',
        'Builder': 'ASJ',
        'Trivia': '''First metro -> bus <- for Stockholm.''',
    }),
)

verymuchabusnotatrain1 = RoadVehicle(
    **COMMON_C1_PROPS,
    id='s_e_C1_2',
    name='All-terrain',
    liveries=make_psd_cc_liveries(
        'pp/1949_SE_C1.psd',
        shading='C1',
        paint='SS',
        overlay=('Lights',),
        cc_replace=colours["GREEN"],
        cc2_replace=colours["GREEN"]
    ),
    company='ss',
    road_type=all_terrain_bus,
    introduction_date=date(1949, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'SS/SL',
        'Use': 'Sockholm Metro buses',
        'Builder': 'ASJ',
        'Trivia': '''First metro -> bus <- for Stockholm.''',
    }),
)

verymuchabusnotatrain2 = RoadVehicle(
    **COMMON_C1_PROPS,
    id='s_e_C1_3',
    name='Highway',
    liveries=make_psd_cc_liveries(
        'pp/1949_SE_C1.psd',
        shading='C1',
        paint='SS',
        overlay=('Lights',),
        cc_replace=colours["GREEN"],
        cc2_replace=colours["GREEN"]
    ),
    company='ss',
    road_type=highway_bus,
    introduction_date=date(1949, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'SS/SL',
        'Use': 'Sockholm Metro buses',
        'Builder': 'ASJ',
        'Trivia': '''First metro -> bus <- for Stockholm.''',
    }),
)

COMMON_CR112_PROPS = dict(
    length=8,
    misc_flags=RoadVehicle.Flags.USE_2CC,
    power_type='3rd',
    max_speed=RoadVehicle.kmhish(90),
    power=25,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=10,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=79,
    loading_speed=40,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    country='sweden',
)

s_b_CR112_1 = RoadVehicle(
    **COMMON_CR112_PROPS,
    id='s_b_CR112_1',
    name='њSL CR112 (1-1-1)',
    liveries=make_psd_cc_liveries(
        'pp/CR112.psd',
        shading='CR112_1-1-1',
        paint='SL1',
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    company='sl',
    road_type=highway_bus,
    introduction_date=date(1978, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'SL',
        'Use': 'Suburban bus',
        'Builder': 'Scania',
        'Trivia': '''First metro -> bus <- for Stockholm.''',
    }),
)

s_b_CR112_2 = RoadVehicle(
    **COMMON_CR112_PROPS,
    id='s_b_CR112_2',
    name='њSL CR112 (2-2-1)',
    liveries=make_psd_cc_liveries(
        'pp/CR112.psd',
        shading='CR112_2-2-1',
        paint='SL1',
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    company='sl',
    road_type=highway_bus,
    introduction_date=date(1978, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'SL',
        'Use': 'Suburban bus',
        'Builder': 'Scania',
        'Trivia': '''First metro -> bus <- for Stockholm.''',
    }),
)

s_b_CR112_3 = RoadVehicle(
    **COMMON_CR112_PROPS,
    id='s_b_CR112_3',
    name='њSL CR112 (1-1-1)',
    liveries=make_psd_cc_liveries(
        'pp/CR112.psd',
        shading='CR112_1-1-1',
        paint='SL2',
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    company='sl',
    road_type=highway_bus,
    introduction_date=date(1988, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'SL',
        'Use': 'Suburban bus',
        'Builder': 'Scania',
        'Trivia': '''First metro -> bus <- for Stockholm.''',
    }),
)

s_b_CR112_4 = RoadVehicle(
    **COMMON_CR112_PROPS,
    id='s_b_CR112_4',
    name='њSL CR112 (2-2-1)',
    liveries=make_psd_cc_liveries(
        'pp/CR112.psd',
        shading='CR112_2-2-1',
        paint='SL2',
        cc_replace=colours["RED"],
        cc2_replace=colours["GREY1"]
    ),
    company='sl',
    road_type=highway_bus,
    introduction_date=date(1978, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'SL',
        'Use': 'Suburban bus',
        'Builder': 'Scania',
        'Trivia': '''First metro -> bus <- for Stockholm.''',
    }),
)

COMMON_7900E_1_PROPS = dict(
    length=8,
    misc_flags=RoadVehicle.Flags.USE_2CC,
    power_type='3rd',
    max_speed=RoadVehicle.kmhish(90),
    power=27,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=14,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=71,
    loading_speed=40,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    country='sweden',
)

s_b_7900E_1_1_VT = RoadVehicle(
    **COMMON_7900E_1_PROPS,
    id='s_b_7900E_1_1_VT',
    name='њVT 7900E (2-2-2)',
    liveries=make_psd_cc_liveries(
        'pp/7900E.psd',
        shading='7900E (2-2-2) Västtrafik',
        cc_replace=colours["SLBLUE"],
        cc2_replace=colours["SKY"]
    ),
    company='sl',
    road_type=highway_bus,
    introduction_date=date(2022, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'Västtrafik',
        'Use': 'City bus',
        'Builder': 'Volvo',
        'Trivia': '''First metro -> bus <- for Stockholm.''',
    }),
)



s_b_7900E_1_2_ST = RoadVehicle(
    **COMMON_7900E_1_PROPS,
    id='s_b_7900E_1_2_ST',
    name='њST 7900E (2-2-2)',
    liveries=make_psd_cc_liveries(
        'pp/7900E.psd',
        shading='7900E (2-2-2) Skånetrafiken',
        paint= ['Window extension'],
        overlay= ['Black lights'],
        cc_replace=colours["GREEN"],
        cc2_replace=colours["GREEN"]
    ),
    company='sl',
    road_type=highway_bus,
    introduction_date=date(2022, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'Skånetrafiken',
        'Use': 'City bus',
        'Builder': 'Volvo',
        'Trivia': '''First metro -> bus <- for Stockholm.''',
    }),
)

s_b_7900E_1_3_JLT = RoadVehicle(
    **COMMON_7900E_1_PROPS,
    id='s_b_7900E_1_3_JLT',
    name='њJLT 7900E (2-2-2)',
    liveries=make_psd_cc_liveries(
        'pp/7900E.psd',
        shading='7900E (2-2-2)',
        paint= ['JLT', 'Window extension'],
        overlay=['JLT leaves', 'Black lights'],
        cc_replace=colours["GREY1"],
        cc2_replace=colours["RED"]
    ),
    company='sl',
    road_type=highway_bus,
    introduction_date=date(2022, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'Jönköpings Länstrafik',
        'Use': 'City bus',
        'Builder': 'Volvo',
        'Trivia': '''First metro -> bus <- for Stockholm.''',
    }),
)

COMMON_7900E_2_PROPS = dict(
    length=8,
    misc_flags=RoadVehicle.Flags.USE_2CC,
    power_type='3rd',
    max_speed=RoadVehicle.kmhish(90),
    power=27,
    vehicle_life=30,
    model_life=30,
    climates_available=grf.ALL_CLIMATES,
    weight=14,
    tractive_effort_coefficient=80,
    running_cost_factor=200,
    cargo_capacity=79,
    loading_speed=40,
    cost_factor=25,
    refittable_cargo_classes=grf.CargoClass.PASSENGERS,
    country='sweden',
)

s_b_7900E_2_1_SB = RoadVehicle(
    **COMMON_7900E_2_PROPS,
    id='s_b_7900E_2_1_SB',
    name='њSB 7900E (2-2-0)',
    liveries=make_psd_cc_liveries(
        'pp/7900E.psd',
        shading='7900E (2-2-0)',
        paint= ['Window extension'],
        overlay=['Black lights'],
        cc_replace=colours["GREY1"],
        cc2_replace=colours["LIME"]
    ),
    company='sl',
    road_type=highway_bus,
    introduction_date=date(2022, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'Skellefteå Buss',
        'Use': 'City bus',
        'Builder': 'Volvo',
        'Trivia': '''First metro -> bus <- for Stockholm.''',
    }),
)

(g.add(lib.SetPurchaseOrder(
    s_b_7900E_2_1_SB
).set_variant_callbacks(g)))

grf.main(g, "buses.grf")