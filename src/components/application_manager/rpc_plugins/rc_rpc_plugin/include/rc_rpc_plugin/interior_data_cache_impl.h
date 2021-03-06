/*
 * Copyright (c) 2018, Ford Motor Company
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *
 * Redistributions of source code must retain the above copyright notice, this
 * list of conditions and the following disclaimer.
 *
 * Redistributions in binary form must reproduce the above copyright notice,
 * this list of conditions and the following
 * disclaimer in the documentation and/or other materials provided with the
 * distribution.
 *
 * Neither the name of the Ford Motor Company nor the names of its contributors
 * may be used to endorse or promote products derived from this software
 * without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
 * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 */

#ifndef SRC_COMPONENTS_APPLICATION_MANAGER_RPC_PLUGINS_RC_RPC_PLUGIN_INCLUDE_RC_RPC_PLUGIN_INTERIOR_DATA_CACHE_IMPL_H_
#define SRC_COMPONENTS_APPLICATION_MANAGER_RPC_PLUGINS_RC_RPC_PLUGIN_INCLUDE_RC_RPC_PLUGIN_INTERIOR_DATA_CACHE_IMPL_H_

#include <map>

#include "rc_rpc_plugin/interior_data_cache.h"
#include "utils/lock.h"
#include "utils/macro.h"

namespace rc_rpc_plugin {
class InteriorDataCacheImpl : public InteriorDataCache {
 public:
  InteriorDataCacheImpl();

  ~InteriorDataCacheImpl();

  void Add(const ModuleUid& module,
           const smart_objects::SmartObject& module_data) OVERRIDE;
  smart_objects::SmartObject Retrieve(const ModuleUid& module) const OVERRIDE;

  std::vector<ModuleUid> GetCachedModulesByType(
      const std::string& module_type) const OVERRIDE;

  bool Contains(const ModuleUid& module) const OVERRIDE;
  void Remove(const ModuleUid& module) OVERRIDE;
  void Clear() OVERRIDE;

 private:
  std::map<ModuleUid, smart_objects::SmartObject> cached_data_;
  mutable sync_primitives::Lock cached_data_lock_;
};

}  // namespace rc_rpc_plugin

#endif  // SRC_COMPONENTS_APPLICATION_MANAGER_RPC_PLUGINS_RC_RPC_PLUGIN_INCLUDE_RC_RPC_PLUGIN_INTERIOR_DATA_CACHE_IMPL_H_
