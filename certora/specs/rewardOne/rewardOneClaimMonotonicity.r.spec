/////////////////////////////////////////////////////////////////////////////////
// Ensure get more rewards with more time
/////////////////////////////////////////////////////////////////////////////////
rule rewardOneClaimMonotonicityTime(address[] assets, address user, address reward) {
    require assets.length == 1;

    address[] rewards = getRewardsByAsset(assets[0]);
    require rewards.length == 1;
    require rewards[0] == Reward;

    // added requirement to reduce timeout
    require getAssetDecimals(assets[0]) == 6;

    env _e; env e_;
    mathint _claimable = getUserRewards(_e, assets, user, reward);
    mathint claimable_ = getUserRewards(e_, assets, user, reward);

    assert _e.block.timestamp <= e_.block.timestamp => _claimable <= claimable_;
}

/////////////////////////////////////////////////////////////////////////////////
// Ensure get more rewards with more AToken
/////////////////////////////////////////////////////////////////////////////////
rule rewardOneClaimMonotonicityAssets(env e, address[] assets, address user, uint256 amount) {
    require assets.length == 1;
    require assets[0] == AToken;

    address[] rewards = getRewardsByAsset(AToken);
    require rewards.length == 1;
    require rewards[0] == Reward;

    mathint _claimable = getUserRewards(e, assets, user, Reward);
    AToken.transfer(e, user, amount);
    mathint claimable_ = getUserRewards(e, assets, user, Reward);

    assert claimable_ >= _claimable;
}

/////////////////////////////////////////////////////////////////////////////////
// Ensure get more rewards with more emission per second
/////////////////////////////////////////////////////////////////////////////////
rule rewardOneClaimMonotonicityEmission(env e, address[] assets, address user, uint256 amount) {
    require assets.length == 1;
    require assets[0] == AToken;

    address[] rewards = getRewardsByAsset(AToken);
    require rewards.length == 1;
    require rewards[0] == Reward;

    uint88[] _emissionsPerSeconds;
    uint88 _emissionsPerSecond = _emissionsPerSeconds[0];
    setEmissionPerSecond(e, AToken, rewards, _emissionsPerSeconds);

    mathint _claimable = getUserRewards(e, assets, user, Reward);

    uint88[] emissionsPerSeconds_;
    uint88 emissionsPerSecond_ = emissionsPerSeconds_[0];
    setEmissionPerSecond(e, AToken, rewards, emissionsPerSeconds_);

    mathint claimable_ = getUserRewards(e, assets, user, Reward);

    assert emissionsPerSecond_ >= _emissionsPerSecond => claimable_ >= _claimable;
}
