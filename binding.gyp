{
  "targets": [
    {
      "target_name": "native_rt",
      "sources": [ "src/cpp/native-rt.cc" ],
      "conditions":[
      	["OS=='linux'", {
      	  "sources": [ "src/cpp/native-rt_linux.cc" ]
      	  }],
      	["OS=='mac'", {
      	  "sources": [ "src/cpp/native-rt_mac.cc" ]
      	}],
        ["OS=='win'", {
      	  "sources": [ "src/cpp/native-rt_win.cc" ]
      	}]
      ]
    }, 
    # IMPORTANT:  This action is critical for a node-pre-gyp module, 
    # it makes sure the binary is placed into the correct directory
    # so requiring apps can find it (see index.js)
    {
      "target_name": "action_after_build",
      "type": "none",
      "dependencies": [ "<(module_name)" ],
      "copies": [
        {
          "files": [ "<(PRODUCT_DIR)/<(module_name).node" ],
          "destination": "<(module_path)"
        }
      ]
    }
  ]
}