# Release verification

Checked October 23, 2026.

## Automated checks

The release passes 32 accounting tests and 10 QR/label tests. The tests cover money rounding, 0% and 100% commissions, mixed ownership, insufficient stock, historical tax and commission snapshots, partial refunds, manual item recovery, owner repayments, audited corrections, unknown costs, date-filtered reports, tax reserves, and invalid backup data.

Label tests encode and decode actual QR matrices at the intended thermal-label scale, check 50 × 30 mm print-page layout, constrain long names and prices, escape user-entered text, and verify the bundled upstream library hashes.

The generated HTML contains one intact application script. The JavaScript bundle and service worker pass syntax checks. The ready-to-upload app uses bundled libraries without runtime CDN requests.

Run the included tests with:

```sh
node tests/core.test.cjs
node tests/labels.test.cjs
```

## Browser checks

Synthetic records were used in a separate preview workspace. They are not included in the release.

- Visually inspected the final dark gaming-and-sports theme on the overview, inventory table, reports, and inventory dialog. Confirmed navigation and form controls remained usable after the styling update.
- Added a commission customer and a partner at 0% store commission.
- Created business and personal inventory with required owner selection.
- Generated and visually inspected a QR price label with its item name, price, human-readable code, and Before tax note.
- Recorded a mixed sale with quantities, a discount, tax, and a processing fee. A $95 merchandise sale produced $7.60 tax, $55 store revenue, $40 owner proceeds, and $34 business operating profit with $20 business merchandise cost and a $1 fee.
- Recorded an owner payout, refunded that owner's product, restored the stock, and recorded the owner's $40 repayment.
- Recorded a 0% partner manual sale, then reversed it with the item recovered. The owner's sales, profit, cost, and balance all returned to zero without a false inventory loss.
- Recorded and voided a mistaken inventory loss. The stock returned once, and the original loss stayed visible as Voided with its reason.
- Reloaded the page and verified persisted records.
- Entered the printed QR payload through the scanner-compatible search field and verified the correct item and tax were added to the cart.
- Downloaded a full JSON backup, changed a store setting, restored the backup through the app, and verified the original settings and balances.
- Downloaded sales CSV and verified that sale/refund lines totaled $45 merchandise and $3.60 tax after the test returns.

## Checks that require the shop's equipment

No physical NELKO printer, label alignment, camera hardware, or handheld scanner was available in this environment. Print one label at 50 × 30 mm and 100% scale, then scan it before a production batch. The phone workflow uses exported PNG files and the printer's companion app.

The offline service worker is included. Test opening the final hosted address online and then offline on the shop's actual browser before relying on offline access. A live GitHub Pages deployment has not been created as part of this package.

The Eldorado tax presets need verification against the shop's complete street address. Income-tax reserve rates are user-configured planning percentages, not calculated tax liabilities.
