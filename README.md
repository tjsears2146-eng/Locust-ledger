# Locust Ledger

Locust Ledger is a browser-based inventory and sales recorder for a shop in Eldorado, Illinois. It handles business-owned merchandise, partners' personal items, and commission customers in one workspace. Products have printable QR price labels, and each sale records the applicable sales tax, store revenue, and proceeds owed to the merchandise owner.

The ready-to-use app is `index.html` at the top level of the ZIP. Its companion `sw.js` enables offline loading after the hosted app has been opened online. The app requires no installation, account, paid database, or cloud service. Printing on a computer requires the printer's driver; phone printing uses the NELKO companion app.

**Records stay in the current browser on the current device.** There is no automatic synchronization or cloud backup. The app records payments completed elsewhere; it does not charge cards, send refunds, transfer owner payouts, or submit tax payments.

**Deployment status:** the project is prepared for upload. These files do not mean a GitHub repository or live GitHub Pages site has already been created.

## Publish on GitHub Pages

No build tools are needed to publish the supplied release. Unzip it first so you can upload the individual files.

1. Sign in to GitHub and create or open the repository you want to use, such as `locust-ledger`. A public repository can use GitHub Pages with GitHub Free.
2. In the repository, use **Add file > Upload files**. Upload the ZIP's top-level `index.html`, `sw.js`, and `THIRD_PARTY_NOTICES.txt` into the repository's top level. Keep these exact filenames. You can also upload `README.md`, `src/`, `vendor/`, `tests/`, and `build.py` if you want the source project in GitHub.
3. Commit the uploaded files to the `main` branch, or your chosen publishing branch.
4. Open **Settings > Pages**. Under **Build and deployment**, choose **Deploy from a branch**. Select your branch and **/(root)**, then **Save**.
5. Wait for the deployment to finish, then open the website link shown on the Pages screen. A project site normally uses `https://YOUR-USERNAME.github.io/YOUR-REPOSITORY/`.
6. Bookmark that exact website address in the browser you will use at the shop. Open it online before relying on offline access.

The ZIP is already arranged for this upload method. Upload its contents so that `index.html` is at the repository root, not inside a containing folder. The source files can remain alongside the ready-to-use app. GitHub's branch publishing selector accepts the root or a `docs` folder; these instructions use the root. See [GitHub's publishing instructions](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

Publish app files only. Do not upload business backup JSON files, reports, or receipt information into a public repository. Visitors to the app get their own empty browser workspace; your locally stored records are not included in the app code.

To update an existing installation, download a full backup first, replace the published `index.html` and `sw.js` together, wait for deployment, and reload the same website address while online. A repository rename, different hosting domain, different browser, or different browser profile may open a different workspace. Move records with a full backup and restore when changing locations.

## Design

The interface blends tabletop gaming and sports collectibles: charcoal surfaces, crimson actions, gold details, a faceted dice mark, and scoreboard-style business totals. The visual theme carries through inventory, owner accounts, reports, and forms. Thermal labels use a crisp black-on-white layout.

## Set up the shop

1. Open **Settings** and enter your store name and complete street address. The supplied address text is a placeholder, not a verified tax location.
2. Verify the tax rates for the exact shop address using the Illinois lookup described below. Review the merchandise categories, then mark the address verification checkbox and save.
3. Open **People > Add person** for each partner or commission customer. Enter their name, relationship, and the percentage of their sales retained by the store.
4. Add inventory. Every new item requires an answer to **Who owns this item?** Choose **Business** or a named person. A new person can also be added from this inventory form.
5. Enter the selling price before tax, quantity, tax category, and cost per unit when known. Create a label and check one physical print before printing a batch.
6. Download a full backup after setup and at the end of each working day.

Use a regular browser window with local storage enabled. The app has no employee login or separate access permissions. Anyone using that browser profile can view and change its records.

## Business and personal ownership

| Inventory owner | Store's share | How it appears in the accounts |
| --- | --- | --- |
| Business | All merchandise proceeds before tax | Store revenue, with the business's item costs deducted when sold |
| Partner selling personal items | Set to 0% for the agreed personal-sales arrangement | All merchandise proceeds belong to that person; their own costs affect their personal profit |
| Commission customer | Any percentage from 0% through 100% | The store earns its percentage; the remainder is owed to the customer |

The relationship label identifies the person. The **Store's share of sales (%)** field controls the actual calculation for both kinds of person. Selecting Partner does not allocate a share of the shop's overall profit, and this app does not calculate partnership ownership distributions.

Commission is calculated on merchandise proceeds after line discounts and before sales tax. For example, a $100 taxable item with an 8% tax rate and a 20% store share produces a $108 customer total: $8 sales tax, $20 store revenue, and $80 owner proceeds. The owner's own purchase cost reduces their personal profit, not the $80 proceeds owed by the store.

Changes to a person's commission affect future sales. Each saved sale retains its original owner, price, cost, commission, and tax rate.

## Inventory and QR codes

Use **Inventory** to search by item name, owner, or printed code. Each item receives a stable code such as `LL-ABCDEF123456`. The QR contains only `LL1:` followed by that code. It does not contain the owner's identity, item cost, commission, or sale price.

The label shows the product name, selling price before tax, and human-readable item code. Scanning looks up the product in the current workspace. It is not a public product web address, so a general phone camera may display its text without opening an item page. Open the app's scanner to add it to a sale.

Use **Label** beside an item to preview, print, save, or share its PNG. Select multiple inventory checkboxes and use **Print selected labels** for a batch. Choose a copy count per item; a batch can contain up to 500 labels. Reprint the visible price label whenever the selling price changes. Its QR still identifies the same inventory item.

Use **Edit > Add stock** for more units with the same owner and unit cost. Create a separate inventory entry when the owner or unit cost differs. Once an item has sales or loss history, its owner and cost are fixed to protect the saved accounting. Archived items retain their history and recorded stock; archiving is not a stock write-off. Use **Record loss** to remove missing, damaged, or discarded units.

## Record a sale

Open **Record a sale** and add items using any of these methods:

- Search and choose an inventory item.
- Choose **Scan QR**, allow camera access, and point the camera at a label. One successful scan adds one unit. Hosted camera access requires HTTPS and browser support.
- In the scan dialog, choose a sharp photo of a label or type its printed item code and select **Find item**.
- Use a handheld QR scanner configured as a keyboard. Focus the sale search field and scan; configure the scanner to send Enter after the code.
- Choose **One-off item** for a manual sale. Enter the description, owner, quantity, price, optional cost, and tax category. This adds a sale line without creating inventory or a printable inventory label.

Review quantities, unit prices, line discounts, and tax categories. The summary separates the customer total, store revenue, and personal owner proceeds. Record the payment method, date, reference, and any processing fee paid by the store.

Complete payment with cash or your existing payment provider, then choose **Record completed sale**. This saves the transaction and reduces inventory. Selecting Card records the method only. Do not enter card numbers into notes or references.

A saved sale can be opened from the overview or reports. **Print record** produces an internal sales record. Correct a saved sale through a refund/reversal and a replacement sale so the original history remains available.

## Reports, costs, and profit

The **Business overview** shows this month's merchandise sales across all owners, store revenue, business operating profit, and stock counts. Owner balances and unremitted sales tax use all recorded activity. **Reports** offers business or individual views with today, month, quarter, year, all-time, or custom dates.

The app uses these accounting relationships:

- **Store revenue:** business-owned merchandise sales plus the store's commissions, after returns and excluding sales tax.
- **Business operating profit:** store revenue less business-owned goods sold, business operating expenses, recorded sale processing fees, and business inventory losses.
- **Personal operating profit:** that person's proceeds after commission, less their own goods sold, expenses, and inventory losses.
- **Owner balance:** proceeds earned less payouts already recorded, adjusted for refunds and money returned by the owner.
- **Sales-tax balance:** tax collected less refunded tax and tax remittances already recorded.

Sales tax and other owners' proceeds are not store earnings. Paying an owner settles a balance; it does not create another operating expense. Paying sales tax or estimated income tax also does not reduce operating profit in these reports. The app is not a bank balance or complete cash-flow statement.

### Enter costs before selling

A blank item cost means **unknown**. Enter `0` only if the item truly cost nothing. If a relevant sold or lost item has an unknown cost, the affected report shows **Cost missing** or **Not available** for profit and reserves. Revenue, tax, and proceeds balances remain available. An unknown cost belonging to a commission customer affects that customer's profit, rather than treating their merchandise as a store purchase.

Enter known costs before recording a sale. Saved sales retain the costs entered at that time, including an unknown cost. Changing inventory later cannot fix an unknown cost already saved on a sale. Use separate inventory entries for stock purchased at different costs.

Stock purchases remain inventory until sold or written off. Enter their unit costs on the inventory item. Use **Expenses & losses** for rent, utilities, supplies, repairs, and other operating costs, choosing the business or relevant person. Do not enter the same stock purchase as an operating expense, or repeat a processing fee already entered on a sale.

Inventory quantities and valuation describe current stock, even when a report uses historical dates. Sales and refunds appear on their respective recorded dates. A refund in a later month affects that later month. The six-month trend always shows the last six calendar months.

Use **Export inventory CSV**, **Export sales CSV**, and **Export summary CSV** for spreadsheet review. Reports respect the selected owner and dates. A person's on-screen sales list can show a mixed-owner receipt's full total; the report metrics and exported line items apply to the selected person. CSV files are reports, not a complete restorable backup.

## Refunds, payouts, and money returned

Open the original sale and choose **Record refund / reversal**. Enter quantities, the refund date, and a reason or external reference. Refunds reverse the original merchandise amount, tax, commission, and owner proceeds, including the original discount allocation.

For an inventory item actually returned in saleable condition, leave **Return to inventory** checked. This restores its stock and reverses its recorded cost of goods sold. If unchecked, its original cost becomes a recorded inventory loss.

For a manual item, the checked option is **Item / cost recovered (no inventory entry)**. Leave it checked when the item or its cost has been recovered. This reverses the recorded cost without creating stock or a loss. Uncheck it when that cost was lost; the refund then records the original cost as a loss. If you want to track a returned manual item as stock, add a new inventory entry separately.

Original card-processing fees remain recorded because the processor may retain them. The app records the refund; make the actual payment through the original payment method separately.

To pay a merchandise owner, open **People > View account > Record payout** after paying them. Record the date, amount, method, and reference. The app prevents paying more than the available proceeds balance.

If an already-paid sale is refunded, the owner's balance may become negative. For example, paying $80 to an owner and later fully refunding that sale leaves $80 recoverable from the owner. Their account then offers **Record money returned**. Use it after they repay the store. Later owner earnings can also offset the negative balance. A recovery is a settlement, not a new sale or additional store income.

### Correct a mistaken expense, payment, or inventory-loss entry

Use **Void entry** for a mistakenly recorded expense, owner payout, money returned by an owner, sales-tax remittance, estimated-tax payment, or manual inventory write-off. Enter the required reason and confirm. The original entry remains in the history marked **Voided**, with an audit record of the correction, and is excluded from financial totals. For expenses, **Void entry** appears beside **Correct**; a voided expense cannot be edited.

Voiding a manual inventory write-off also restores its quantity to recorded stock. A loss created automatically by a refund stays attached to that refund and cannot be voided separately.

Voiding corrects the bookkeeping only. It does not move cash, reverse a bank or card transaction, send money back to an owner, or undo a payment to a taxing authority. Use it when the saved entry is wrong, and record any actual payment, repayment, or refund through its appropriate workflow. If a corrected entry is needed, add it with the accurate details after voiding the mistaken one.

## Eldorado sales tax and income-tax planning

### Initial sales-tax categories

Rates were reviewed on **October 23, 2026** against Illinois Department of Revenue municipality files for **Eldorado, location 083-0004-6**:

| Category | Initial combined rate | Use |
| --- | ---: | --- |
| General merchandise | 8.00% | Ordinary taxable merchandise; includes 6.25% statewide tax and 1.75% additional local taxes |
| Qualifying groceries | 1.00% | Eldorado's local grocery tax on qualifying groceries |
| Exempt | 0.00% | Only where a valid exemption applies |

These are starting presets. A mailing city or ZIP code does not establish the tax jurisdiction of an exact street address. In **Settings**, verify your complete shop address through [Illinois tax-rate resources](https://tax.illinois.gov/research/taxrates.html) and [MyTax Illinois](https://mytax.illinois.gov/), then confirm the applicable product categories. Do not add another 6.25% to the 8% combined category.

Illinois ended its statewide 1% grocery tax on January 1, 2026; Eldorado's 1% local grocery rate remains relevant. Candy, soft drinks, and food prepared for immediate consumption generally use the general-merchandise category rather than the qualifying-grocery rate. The app does not infer a product's tax treatment from its name. See [Illinois's grocery-tax bulletin](https://tax.illinois.gov/research/publications/bulletins/fy-2026-03.html) and [food classification guidance](https://tax.illinois.gov/research/publications/pio-115.html).

For ordinary taxable consignment sales recorded here, sales tax applies to the taxable retail selling price, before the proceeds are divided between the store and owner. A 0% store commission or personal owner assignment is not a sales-tax exemption. See the [Illinois consignment-sales rule](https://ilga.gov/commission/jcar/admincode/086/086001300S19150R.html).

Add or edit categories for another verified combined rate. Review rates before use, when the shop moves, and when applicable tax rules change. Future sales use the new settings; historical sales and refunds preserve their recorded rates. The app has no live tax-service connection and does not determine every product-specific tax or out-of-state delivery obligation.

The official files used for the initial review are the [current general sales-tax municipality file](https://tax.illinois.gov/content/dam/soi/en/web/tax/research/taxrates/documents/salestaxrates/ordmache-current.txt) and [current grocery-tax municipality file](https://tax.illinois.gov/content/dam/soi/en/web/tax/research/taxrates/documents/salestaxrates/grocerymache-current.txt). These URLs are updated by Illinois, so recheck their current contents when reviewing rates.

In **Reports**, use **Record tax remittance** only after making a sales-tax payment. Keep its period or confirmation reference. This updates the recorded balance; the app does not file the return or send the payment.

### Federal and Illinois income-tax reserves

There is no blanket federal retail sales-tax percentage added to ordinary merchandise in this setup. Federal income-tax planning is separate from customer sales tax. Particular goods can have excise-tax rules; the app does not automatically classify those. The IRS describes these categories in its [business-tax overview](https://www.irs.gov/businesses/business-taxes) and [excise-tax guidance](https://www.irs.gov/businesses/small-businesses-self-employed/excise-tax).

Business reserve estimates start disabled. Enable them in **Settings** and enter your chosen federal and Illinois percentages. Each person's profile has separate reserve settings. A reserve is the chosen percentage of positive recorded operating profit for the report period. It is zero for a known loss and unavailable when relevant costs are missing. Changing percentages recalculates these planning estimates.

These reserves do not calculate actual tax liability, brackets, self-employment tax, entity tax treatment, other income, deductions, or credits. Choose percentages that suit your tax planning. **Record estimated-tax payment** logs a payment already made and keeps it separate from operating expenses.

## NELKO PM220 label-printer setup

The label preset is **50 mm wide by 30 mm high**, with a horizontal layout, QR on the left, and product name and price on the right. PNG exports are 400 by 240 pixels. Use white direct-thermal adhesive labels sized 50 × 30 mm.

Official advertised US prices checked **October 23, 2026**, before tax and shipping:

| Item | Price | Official link |
| --- | ---: | --- |
| NELKO PM220, white | $42.99 | [Printer product page](https://nelko.com/products/nelko-pm220-label-printer) |
| PM220-compatible 50 × 30 mm white labels, one roll | $12.99 | [Label product page](https://nelko.com/products/nelko-labels-for-pm220-2-x-1-18-50x30mm-thermal-sticker-label-1-roll-of-230-self-adhesive-thermal-paper-white) |

Prices and availability can change. Nothing has been purchased. Match the exact **50 × 30 mm** size when ordering; the manufacturer's visible inch-based product heading is rounded. The PM220 uses thermal paper, with no ink or toner, and has official Windows and Mac driver downloads. [NELKO's PM220 support page](https://nelko.com/pages/support-pm220) provides drivers and the manual.

### Windows or Mac computer

1. Install the current PM220 driver for your operating system from NELKO's support page. Connect the printer by USB and load the 50 × 30 mm labels following its manual.
2. Set the printer's label or custom paper size to **50 mm width, 30 mm height**. Calibrate label feeding if needed.
3. In Locust Ledger, open an item's **Label** and choose **Print labels**, or use a selected-item batch.
4. Select the PM220 in the browser or system print dialog. Use **100% / Actual size**, **0 margins**, and turn **headers and footers off**. Preserve the wide 50 × 30 mm layout; driver orientation names vary, so check the preview. Disable fit-to-page scaling.
5. Print one label. Check that no edge is clipped, the price is legible, and the app can scan the QR. Adjust the printer's alignment or density if necessary before printing a batch.

If the browser blocks the print window, allow popups for the app and try again. If the size setting is missing, open the system print dialog or printer preferences to create the custom label size. Do not shrink the QR or crop its white border to compensate for incorrect paper settings.

### iPhone, iPad, or Android phone

1. Install NELKO's supported companion app and connect the PM220 inside that app, following [NELKO's connection and image-import guidance](https://nelko.com/pages/faq-nelko).
2. In Locust Ledger, open the product's **Label** and choose **Save PNG** or **Share PNG**, depending on your browser's sharing support. Save the original image to a location the NELKO app can access.
3. Create a 50 × 30 mm layout in NELKO, import the saved label as an image, preserve the complete image and its aspect ratio, and print from NELKO.
4. Print and scan one sample before repeating copies. Use the exported PNG rather than a screenshot of the preview.

This phone workflow does not provide direct Bluetooth printing from the browser or promise AirPrint support. Printed-label alignment and real camera performance still require a test with your actual device and printer; software QR decoding tests are not hardware validation.

## Backups, restore, and offline use

**Settings > Download full backup** exports all saved inventory, people, transactions, refunds, expenses, payouts, losses, tax records, settings, and change history as one JSON file. Confirm that the download actually completed. A displayed backup timestamp records the download request, not independent verification that the file is safely stored.

Keep dated backup copies somewhere you control, preferably on another device or your own storage service. Back up at least after each working day, before changing site addresses or browsers, and before restoring or updating the app. Backup files contain the business's financial information. An unfinished sale is a temporary draft, not a completed transaction in the full backup.

To recover or move the workspace, open **Settings > Restore backup**, choose a Locust Ledger JSON backup, review the summary, then confirm **Back up current & restore**. Restore starts a download of the current records and replaces the browser workspace with the selected backup. It does not merge two devices' changes. The import limit is 50 MB. CSV reports cannot be restored as a workspace.

Browser data is separate for each device, browser profile, and website location. Clearing site data, losing the device, or using a temporary/private browsing session can remove access to records. There is no password-protected server copy to recover automatically. Use one primary device for day-to-day entry; backup and restore is a deliberate transfer method, not multi-device synchronization.

The app stores records in IndexedDB and requests an offline app cache on supported hosted browsers. After opening it online and allowing the page to load, test reopening it without internet before relying on offline use. Browser storage restrictions or cache removal can prevent offline access. A saved HTML file can be useful for viewing the app, but HTTPS hosting is the normal operating setup for camera access and the offline worker.

If a save fails, read the displayed error and keep the current browser data. If another tab has newer records, reload before making further changes. **Settings > View change history** shows recent changes; the full audit history is retained in the backup.

## Source project and local development

The release bundles its JavaScript, CSS, QR encoder, and QR decoder into the top-level `index.html`. The ZIP also contains `sw.js`, this README, the notices, and the complete source project. There is no `dist` folder in the supplied ZIP, and no CDN or package installation is required at runtime.

| Path | Purpose |
| --- | --- |
| `index.html`, `sw.js` | Ready-to-publish app and offline worker |
| `src/core.js` | Money calculations, transaction validation, accounting, and reports |
| `src/storage.js` | Browser-local persistence and protection against conflicting saves |
| `src/labels.js` | QR data, 50 × 30 mm label layout, PNG export, and print pages |
| `src/app.js`, `src/style.css`, `src/shell.html` | Interface and application behavior |
| `vendor/` | Bundled QR libraries and their original license notices |
| `tests/` | Accounting and QR/label tests |
| `build.py` | Regenerates the root app and offline worker, plus copies in `dist/` |

From the project root, rebuild with Python 3:

```sh
python3 build.py
```

The build recreates `index.html` and `sw.js` at the project root and also creates a `dist/` folder for static-hosting workflows. Upload the regenerated root files together when publishing an update.

Run the checks with Node.js:

```sh
node tests/core.test.cjs
node tests/labels.test.cjs
```

For a local preview:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Open `http://localhost:8000/`. Localhost and the final hosted website have separate browser records. Use full backup and restore if moving real data between them. On Windows, `py -3` can replace `python3` if that is how Python is installed.

Third-party components are **qrcode-generator 1.4.4** under the MIT License and **jsQR 1.4.0** under Apache License 2.0. Their complete license text and source provenance are in [THIRD_PARTY_NOTICES.txt](THIRD_PARTY_NOTICES.txt) and the corresponding files under `vendor/`. Keep the notices with redistributed copies of the app.
