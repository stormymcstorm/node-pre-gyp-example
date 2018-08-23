#include <node_api.h>
#include "native-rt.h"

namespace native_rt {

napi_value Method(napi_env env, napi_callback_info args) {
  double time_now = native_now();
  napi_value result;
  napi_status status;

  status = napi_create_double(env, time_now, &result);
  if (status != napi_ok) return nullptr;
  return result;
}

napi_value init(napi_env env, napi_value exports) {
  napi_status status;
  napi_value fn;

  status = napi_create_function(env, nullptr, 0, Method, nullptr, &fn);
  if (status != napi_ok) return nullptr;

  status = napi_set_named_property(env, exports, "now", fn);
  if (status != napi_ok) return nullptr;
  return exports;
}

NAPI_MODULE(NODE_GYP_MODULE_NAME, init)

}  // namespace demo