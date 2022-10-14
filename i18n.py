import bpy

dict = {
    "en_US":{
        (None, "Pick character:"):"Pick character:",
        (None, "Character"):"Character",
        (None, "Pick Bone"):"Pick Bone",
        (None, "Use Picked Bone from ARMATURE"):"Use Picked Bone from ARMATURE",
        (None, "Hip Bone"):"Hip Bone",
        (None, "Head Bone"):"Head Bone",
        (None, "L Eye Bone"):"L Eye Bone",
        (None, "R Eye Bone"):"R Eye Bone",
        (None, "Use Selected Camera"):"Use Selected Camera",
        (None, "Min Length"):"Min Length",
        (None, "Max Length"):"Max Length",
        (None, "Speed(metre per frame)"):"Speed(metre per frame)",
        (None, "Use project frame range"):"Use project frame range",
        (None, "Allow Rotation"):"Allow Rotation",
        (None, "Max Horizontal Angle"):"Max Horizontal Angle",
        (None, "Max Vertical Angle"):"Max Vertical Angle",
        (None, "Lower Shot Chance"):"Lower Shot Chance",
        (None, "CloseUp Shot Chance"):"CloseUp Shot Chance",
        (None, "The chance of a lower shot is 0.25/this value, bigger value means less of lower shots"):"The chance of a lower shot is 0.25/this value, bigger value means less of lower shots",
        (None, "The chance of a close-up shot is 0.25/this value, bigger value means less of close-up shots"):"The chance of a close-up shot is 0.25/this value, bigger value means less of close-up shots",
        (None, "Shot Length(second):"):"Shot Length(second):",
        (None, "Shot Chance:"):"Shot Chance:",
        (None, "Generate"):"Generate",
        (None, "Export Vmd"):"Export Vmd",
        (None, "Export Daz"):"Export Daz",
        (None, "https://github.com/butaixianran/Blender-Auto-Dance-Camera"):"https://github.com/butaixianran/Blender-Auto-Dance-Camera",
        (None, "Use Audio Beat File"):"Use Audio Beat File",
        (None, "Upper Shot Power"):"Upper Shot Power",
    },
    "zh_CN":{
        (None, "Pick character:"):"选择人模骨架:",
        (None, "Character"):"人模",
        (None, "Pick Bone"):"选择骨骼",
        (None, "Use Picked Bone from ARMATURE"):"使用从骨架上选择的骨骼",
        (None, "Hip Bone"):"髋骨",
        (None, "Head Bone"):"头",
        (None, "L Eye Bone"):"左眼",
        (None, "R Eye Bone"):"右眼",
        (None, "Use Selected Camera"):"使用当前选择的摄影机",
        (None, "Min Length"):"最小长度",
        (None, "Max Length"):"最大长度",
        (None, "Speed(metre per frame)"):"速度(米每帧)",
        (None, "Use project frame range"):"使用项目帧范围",
        (None, "Allow Rotation"):"允许旋转",
        (None, "Max Horizontal Angle"):"最大水平角度",
        (None, "Max Vertical Angle"):"最大垂直角度",
        (None, "Lower Shot Chance"):"下半身镜头概率",
        (None, "CloseUp Shot Chance"):"近景镜头概率",
        (None, "The chance of a lower shot is 0.25/this value, bigger value means less of lower shots"):"下半身镜头概率是0.25除以该值，值越大该镜头出现次数越少",
        (None, "The chance of a close-up shot is 0.25/this value, bigger value means less of close-up shots"):"近景镜头概率是0.25除以该值，值越大该镜头出现次数越少",
        (None, "Shot Length(second):"):"镜头长度(秒):",
        (None, "Shot Chance:"):"镜头出现概率:",
        (None, "Generate"):"生成",
        (None, "Export Vmd"):"导出Vmd",
        (None, "Export Daz"):"导出Daz",
        (None, "https://github.com/butaixianran/Blender-Auto-Dance-Camera"):"https://github.com/butaixianran/Blender-Auto-Dance-Camera/blob/main/README.cn.md",
        (None, "Use Audio Beat File"):"使用音频节拍文件",
        (None, "Upper Shot Power"):"上半身镜头出现倍率",
    },
    "zh_TW":{
        (None, "Pick character:"):"選擇人模骨架:",
        (None, "Character"):"人模",
        (None, "Pick Bone"):"選擇骨骼",
        (None, "Use Picked Bone from ARMATURE"):"使用從骨架上選擇的骨骼",
        (None, "Hip Bone"):"髖骨",
        (None, "Head Bone"):"頭",
        (None, "L Eye Bone"):"左眼",
        (None, "R Eye Bone"):"右眼",
        (None, "Use Selected Camera"):"使用當前選擇的攝影機",
        (None, "Min Length"):"最小長度",
        (None, "Max Length"):"最大長度",
        (None, "Speed(metre per frame)"):"速度(米每幀)",
        (None, "Use project frame range"):"使用項目幀範圍",
        (None, "Allow Rotation"):"允許旋轉",
        (None, "Max Horizontal Angle"):"最大水平角度",
        (None, "Max Vertical Angle"):"最大垂直角度",
        (None, "Lower Shot Chance"):"下半身鏡頭概率",
        (None, "CloseUp Shot Chance"):"近景鏡頭概率",
        (None, "The chance of a lower shot is 0.25/this value, bigger value means less of lower shots"):"下半身鏡頭概率是0.25除以該值，值越大該鏡頭出現次數越少",
        (None, "The chance of a close-up shot is 0.25/this value, bigger value means less of close-up shots"):"近景鏡頭概率是0.25除以該值，值越大該鏡頭出現次數越少",
        (None, "Shot Length(second):"):"鏡頭長度(秒):",
        (None, "Shot Chance:"):"鏡頭出現概率:",
        (None, "Generate"):"生成",
        (None, "Export Vmd"):"輸出Vmd",
        (None, "Export Daz"):"輸出Daz",
        (None, "https://github.com/butaixianran/Blender-Auto-Dance-Camera"):"https://github.com/butaixianran/Blender-Auto-Dance-Camera/blob/main/README.cn.md",
        (None, "Use Audio Beat File"):"使用音頻節拍文件",
        (None, "Upper Shot Power"):"上半身鏡頭出現倍率",
    },
}


def register():
    bpy.app.translations.register(__name__, dict)

def unregister():
    bpy.app.translations.unregister(__name__)

# need register
def word(msg_id):
    return bpy.app.translations.pgettext(msg_id)

# do not need register, but need to reboot blender
def word2(msg_id):
    lang = bpy.app.translations.locale
    msg_key = (None, msg_id)

    word = msg_id
    if lang in dict.keys():
        if msg_key in dict[lang].keys():
            word = dict[lang][msg_key]

    return word


