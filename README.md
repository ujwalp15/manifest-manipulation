# manifest-manipulation

## Various tools to create local manifests for android ROMs


### darwin-delete

> Creates a darwin projects removal manifest for your ROM, helpful
for linux builders short on bandwidth and/or disk space

To use, copy the `delete-darwin.py` file to your working directory, then execute by running `./delete-darwin.py`

To utilise the manifest created

```
mkdir -p .repo/local_manifests/
mv delete_darwin.xml .repo/local_manifests/
repo sync -j$(nproc --all) -c --no-tags --force-sync -f
```

### linux-delete

> Creates a linux projects removal manifest for your ROM, helpful
for darwin builders short on bandwidth and/or disk space

To use, copy the `delete-linux.py` file to your working directory, then execute by running `./delete-linux.py`

To utilise the manifest created

```
mkdir -p .repo/local_manifests/
mv delete_linux.xml .repo/local_manifests/
repo sync -j$(nproc --all) -c --no-tags --force-sync -f
```

### aosp-delete

> Creates a aosp projects removal manifest for your ROM for people
who don't/can't build locally and hence don't want the extra crap
they won't be working on

To use, copy the `delete-aosp.py` file to your working directory, then execute by running `./delete-aosp.py`

To utilise the manifest created

```
mkdir -p .repo/local_manifests/
mv delete_aosp.xml .repo/local_manifests/
repo sync -j$(nproc --all) -c --no-tags --force-sync -f
```

### shallow-prebuilts

> Creates a manifest with all prebuilts set to clone-depth=1 for minimising bandwidth and disk usage

To use, copy the `shallow-prebuilts.py` file to your working directory, then execute by running `./shallow-prebuilts.py`

To utilise the manifest created

```
mkdir -p .repo/local_manifests/
mv shallow_prebuilts.xml .repo/local_manifests/
repo sync -j$(nproc --all) -c --no-tags --force-sync -f
```
