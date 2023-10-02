import "./RewardsController_base.spec";
import "./methods/Methods_more.spec";
import "./common/invariants.i.spec";
import "./common/math.d.spec";
import "./common/harness.d.spec";
import "./common/reverts.f.spec";
import "./common/rewards.f.spec";
import "./common/claim.r.spec";
import "./common/setup.r.spec";
import "./common/zeroAddress.r.spec";
import "./common/rewardsCalculate.f.spec";
import "./rewardsTwo/rewardsTwoClaim.r.spec";
import "./rewardsTwo/rewardsTwo.r.spec";
import "./assetsTwo/assetsTwo.r.spec";

using DummyERC20_rewardTokenB as RewardB;

// SLOW : SOMETIMES TIMEOUT
use invariant rewardEnabled;
use rule noDoubleClaim;
use rule setupAssetImmutable;
use rule rewardsTwoClaimAllRewardsAsExpected;
use rule onlyAuthorizeCanDecrease;
use rule rewardsTwoClaimAllRewardsOnBehalfAsExpected;
use rule rewardsTwoClaimAllRewardsToSelfAsExpected;
use rule setupAssetsAdded;