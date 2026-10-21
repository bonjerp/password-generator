# Minimal dark theme for PassGen
APP_STYLE = """
QWidget { background: #151515; color: #EDEDED; font-family: "Segoe UI"; font-size: 12px; }
#contentWidget { background: #151515; }
#appIcon { color: #8D8D8D; font-size: 10px; font-weight: 700; letter-spacing: 2px; }
#titleLabel { color: #F2F2F2; font-size: 17px; font-weight: 600; }
#passwordCard { background: #202020; border: 1px solid #333333; border-radius: 10px; }
#passwordOutput { background: transparent; border: 0; color: #FAFAFA; font-family: Consolas; font-size: 17px; min-height: 34px; padding: 0 4px; }
#copyButton { background: #303030; border: 1px solid #414141; border-radius: 6px; color: #DADADA; padding: 7px 12px; min-width: 44px; }
#copyButton:hover { background: #404040; }
#copyButton:pressed { background: #282828; }
#strengthSegment { background: #3B3B3B; border: none; border-radius: 2px; }
#strengthSegment[active="true"] { background: #BDBDBD; }
#strengthInfo, #strengthText, #strengthValue { background: transparent; }
#strengthText { color: #949494; font-size: 10px; }
#strengthValue { color: #DADADA; font-size: 10px; font-weight: 600; }
#settingsCard { background: transparent; border: none; }
#lengthTitle, #minimumTitle { color: #DCDCDC; font-size: 12px; font-weight: 600; }
#lengthValue { color: #F2F2F2; font-size: 13px; font-weight: 600; }
#rangeLabel, #minimumOptional { color: #777777; font-size: 10px; }
QSlider { background: transparent; min-height: 17px; }
QSlider::groove:horizontal { background: #383838; height: 4px; border-radius: 2px; }
QSlider::sub-page:horizontal { background: #AFAFAF; border-radius: 2px; }
QSlider::handle:horizontal { background: #E7E7E7; width: 13px; height: 13px; margin: -5px 0; border-radius: 6px; }
QSlider::handle:horizontal:hover { background: white; }
#optionCard { background: #202020; border: 1px solid #303030; border-radius: 8px; min-height: 48px; }
#optionCard:hover { background: #292929; border-color: #515151; }
#optionTitle { background: transparent; color: #E8E8E8; font-size: 12px; font-weight: 500; }
#optionSubtitle { background: transparent; color: #858585; font-size: 10px; }
#minimumLabel { color: #AFAFAF; font-size: 12px; }
#minimumSpin { background: #242424; color: #EAEAEA; border: 1px solid #383838; border-radius: 6px; min-width: 70px; min-height: 27px; padding: 0 8px; }
#minimumSpin:focus { border-color: #898989; }
#minimumSpin:disabled { color: #666666; background: #1B1B1B; }
#generateButton { background: #E8E8E8; color: #171717; border: 0; border-radius: 8px; min-height: 44px; font-size: 13px; font-weight: 700; }
#generateButton:hover { background: #FFFFFF; }
#generateButton:pressed { background: #CCCCCC; }
#toastLabel { background: #303030; color: #F1F1F1; border: 1px solid #525252; border-radius: 6px; padding: 6px 12px; font-weight: 600; }
"""
