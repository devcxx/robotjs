{
  'targets': [{
    'target_name': 'robotjs',
      'cflags!': [ '-fno-exceptions' ],
      'cflags_cc!': [ '-fno-exceptions' ],
      'xcode_settings': { 'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
        'CLANG_CXX_LIBRARY': 'libc++',
        'MACOSX_DEPLOYMENT_TARGET': '10.15',
      },
      'msvs_settings': {
        'VCCLCompilerTool': { 'ExceptionHandling': 1 },
      },
    'include_dirs': [
      '<!(node -p "require(\'node-addon-api\').include_dir")',
    ],
    
    'conditions': [
      ['OS == "mac"', {
        'include_dirs': [
          '<!(node -p "require(\'node-addon-api\').include_dir")',
          'System/Library/Frameworks/CoreFoundation.Framework/Headers',
          'System/Library/Frameworks/Carbon.Framework/Headers',
          'System/Library/Frameworks/ApplicationServices.framework/Headers',
          'System/Library/Frameworks/OpenGL.framework/Headers',
        ],
        'link_settings': {
          'libraries': [
            '-framework Carbon',
            '-framework CoreFoundation',
            '-framework ApplicationServices',
            '-framework OpenGL'
          ]
        },
        'sources': [
          'src/clip_osx.mm'
        ]
      }],
      
      ['OS == "linux"', {
        'link_settings': {
          'libraries': [
            '-lX11',
            '-lXtst'
          ]
        },
        
        'sources': [
          'src/xdisplay.c',
          'src/clip_linux.cc'
        ]
      }],

      ["OS=='win'", {
        'defines': ['IS_WINDOWS'],
        'sources': [
          'src/clip_win.cc'
        ]
      }]
    ],
    
    'sources': [
      'src/robotjs.cc',
      'src/deadbeef_rand.c',
      'src/mouse.c',
      'src/keypress.c',
      'src/keycode.c',
      'src/screen.c',
      'src/snprintf.c'
    ]
  }]
}