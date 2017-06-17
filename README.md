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
