#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rocksdb
Version  : 4.1
Release  : 3
URL      : https://github.com/facebook/rocksdb/archive/v4.1.tar.gz
Source0  : https://github.com/facebook/rocksdb/archive/v4.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: rocksdb-lib
BuildRequires : bzip2-dev
BuildRequires : cmake
BuildRequires : gflags-dev
BuildRequires : snappy-dev
BuildRequires : zlib-dev
Patch1: 0001-Fix-Makefile.patch

%description
This folder defines a REDIS-style interface for Rocksdb.
Right now it is written as a simple tag-on in the rocksdb::RedisLists class.
It implements Redis Lists, and supports only the "non-blocking operations".

%package dev
Summary: dev components for the rocksdb package.
Group: Development
Requires: rocksdb-lib
Provides: rocksdb-devel

%description dev
dev components for the rocksdb package.


%package lib
Summary: lib components for the rocksdb package.
Group: Libraries

%description lib
lib components for the rocksdb package.


%prep
%setup -q -n rocksdb-4.1
%patch1 -p1

%build
make V=1  %{?_smp_mflags} shared_lib

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/rocksdb/c.h
/usr/include/rocksdb/cache.h
/usr/include/rocksdb/compaction_filter.h
/usr/include/rocksdb/compaction_job_stats.h
/usr/include/rocksdb/comparator.h
/usr/include/rocksdb/convenience.h
/usr/include/rocksdb/db.h
/usr/include/rocksdb/db_dump_tool.h
/usr/include/rocksdb/delete_scheduler.h
/usr/include/rocksdb/env.h
/usr/include/rocksdb/experimental.h
/usr/include/rocksdb/filter_policy.h
/usr/include/rocksdb/flush_block_policy.h
/usr/include/rocksdb/immutable_options.h
/usr/include/rocksdb/iostats_context.h
/usr/include/rocksdb/iterator.h
/usr/include/rocksdb/ldb_tool.h
/usr/include/rocksdb/listener.h
/usr/include/rocksdb/memtablerep.h
/usr/include/rocksdb/merge_operator.h
/usr/include/rocksdb/metadata.h
/usr/include/rocksdb/options.h
/usr/include/rocksdb/perf_context.h
/usr/include/rocksdb/perf_level.h
/usr/include/rocksdb/rate_limiter.h
/usr/include/rocksdb/slice.h
/usr/include/rocksdb/slice_transform.h
/usr/include/rocksdb/snapshot.h
/usr/include/rocksdb/sst_dump_tool.h
/usr/include/rocksdb/sst_file_writer.h
/usr/include/rocksdb/statistics.h
/usr/include/rocksdb/status.h
/usr/include/rocksdb/table.h
/usr/include/rocksdb/table_properties.h
/usr/include/rocksdb/thread_status.h
/usr/include/rocksdb/transaction_log.h
/usr/include/rocksdb/types.h
/usr/include/rocksdb/universal_compaction.h
/usr/include/rocksdb/utilities/backupable_db.h
/usr/include/rocksdb/utilities/checkpoint.h
/usr/include/rocksdb/utilities/convenience.h
/usr/include/rocksdb/utilities/db_ttl.h
/usr/include/rocksdb/utilities/document_db.h
/usr/include/rocksdb/utilities/flashcache.h
/usr/include/rocksdb/utilities/geo_db.h
/usr/include/rocksdb/utilities/info_log_finder.h
/usr/include/rocksdb/utilities/json_document.h
/usr/include/rocksdb/utilities/leveldb_options.h
/usr/include/rocksdb/utilities/optimistic_transaction_db.h
/usr/include/rocksdb/utilities/spatial_db.h
/usr/include/rocksdb/utilities/stackable_db.h
/usr/include/rocksdb/utilities/table_properties_collectors.h
/usr/include/rocksdb/utilities/transaction.h
/usr/include/rocksdb/utilities/transaction_db.h
/usr/include/rocksdb/utilities/transaction_db_mutex.h
/usr/include/rocksdb/utilities/utility_db.h
/usr/include/rocksdb/utilities/write_batch_with_index.h
/usr/include/rocksdb/version.h
/usr/include/rocksdb/write_batch.h
/usr/include/rocksdb/write_batch_base.h
/usr/lib64/*.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
