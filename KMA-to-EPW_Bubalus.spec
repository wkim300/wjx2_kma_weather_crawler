# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['KMA-to-EPW_Bubalus.py'],
             pathex=['C:\\Users\\ECODA\\Desktop\\dhwtest\\pyapitest\\vscode\\apicore', 'C:\\Users\\ECODA\\Desktop\\dhwtest\\pyapitest\\vscode'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='KMA-to-EPW_Bubalus',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='swj.ico')
