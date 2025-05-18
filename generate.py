import grf, lib
from datetime import date

g = lib.NewGRF(
    grfid="MEJA", # change
    name="Epic bus grf",
    description="An epic bus grf in grf-py",
    min_compatible_version=0,
    version=0, #should be 1 on release 0 for testing
    id_map_file="ids.json"
)

# roadtype table
(
    slow,
    slow_bus,
    regular,
    regular_bus,
    fast,
    fast_bus,
) = g.set_roadtype_table([
    ('RAAN', 'ROAD'),         #Slow / dirt not suited for motorway due to speed
    ('PAAN', 'RAAN', 'ROAD'), #Bus
    ('RABN', 'ROAD'),         #Regular / allowed everywhere
    ('PABN', 'RABN', 'ROAD'), #Bus
    ('RACN', 'ROAD'),         #Fast / motorway not suited for mud
    ('PACN', 'RACN', 'ROAD'), #Bus
])

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
    length=8,
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
    #id='s_e_C1_1',
    id=0x01,
    name='њSS/SL C1',
    liveries=make_psd_cc_liveries(
        'pp/1949_SE_C1.psd',
        shading='C1',
        paint='SS',
        overlay=('Lights',),
        cc_replace=colours["GREEN"],
        cc2_replace=colours["GREEN"]
    ),
    company='ss',
    road_type=fast_bus,
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
    #id='s_e_C1_1',
    id=0x02,
    name='њSS/SL C1',
    liveries=make_psd_cc_liveries(
        'pp/1949_SE_C1.psd',
        shading='C1',
        paint='SS',
        overlay=('Lights',),
        cc_replace=colours["GREEN"],
        cc2_replace=colours["GREEN"]
    ),
    company='ss',
    road_type=fast,
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
    #id='s_e_C1_1',
    id=0x03,
    name='њSS/SL C1',
    liveries=make_psd_cc_liveries(
        'pp/1949_SE_C1.psd',
        shading='C1',
        paint='SS',
        overlay=('Lights',),
        cc_replace=colours["GREEN"],
        cc2_replace=colours["GREEN"]
    ),
    company='ss',
    road_type=slow,
    introduction_date=date(1949, 1, 1),
    additional_text=grf.fake_vehicle_info({
        'Operator': 'SS/SL',
        'Use': 'Sockholm Metro buses',
        'Builder': 'ASJ',
        'Trivia': '''First metro -> bus <- for Stockholm.''',
    }),
)

grf.main(g, "buses.grf")