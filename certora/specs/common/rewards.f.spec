/////////////////////////////////////////////////////////////////////////////////
// Requirements for ONE reward ONE asset
/////////////////////////////////////////////////////////////////////////////////
function rewardsOneAssetsOne(address asset, address reward) returns bool {
    // mathint decimals = getAssetDecimals(asset);
    address[] assets = getAssetsList();
    address[] rewardsByAsset = getRewardsByAsset(asset);
    address[] rewardsList = getRewardsList();

    return assets.length == 1
        && assets[0] == asset
        // && decimals <= 18 && decimals >= 6
        // && decimals == 6

        && rewardsList.length == 1
        && rewardsList[0] == reward

        && rewardsByAsset.length == 1
        && rewardsByAsset[0] == reward

        && getAvailableRewardsCount(asset) == 1;
}

/////////////////////////////////////////////////////////////////////////////////
// Requirements for TWO rewards ONE asset
/////////////////////////////////////////////////////////////////////////////////
function rewardsTwoAssetsOne(address asset, address reward1, address reward2) returns bool {
    mathint decimals = getAssetDecimals(asset);
    address[] assets = getAssetsList();
    address[] rewardsList = getRewardsList();
    address[] rewardsByAsset = getRewardsByAsset(asset);

    return assets.length == 1
        && assets[0] == asset
        // && decimals <= 18 && decimals >= 6
        && decimals == 6

        && rewardsList.length == 2
        && rewardsList[0] == reward1
        && rewardsList[1] == reward2

        && rewardsByAsset.length == 2
        && rewardsByAsset[0] == reward1
        && rewardsByAsset[1] == reward2

        && getAvailableRewardsCount(asset) == 2;
}

