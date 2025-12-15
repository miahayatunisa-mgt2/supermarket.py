import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from io import BytesIO

# ===================== PAGE CONFIG =====================
st.set_page_config(
    page_title="Supermarket Sales Dashboard",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===================== TEAM INFORMATION =====================
TEAM_INFO = {
    "group_name": "Group 2 - Business Mathematics",
    "members": [
        "Annisa Zein",
        "Dzihni Nailahusna Setiadie", 
        "Esther Gabriella Sianipar",
        "Mia Hayatunisa"
    ]
}

# ===================== THEME COLORS =====================
PRIMARY_START = "#001f3f"  # navy
PRIMARY_END = "#ff0033"    # red-ish
ACCENT_COLOR = "#001f3f"
LINE_COLOR = "#ff0033"

# ===================== TRANSLATIONS =====================
TRANSLATIONS = {
    "English": {
        "title": "SUPERMARKET SALES DASHBOARD",
        "subtitle": "Performance Sales, Deals Analysis, and Business Insights Dashboard",
        "team_info": f"{TEAM_INFO['group_name']}",
        "members": " | ".join(TEAM_INFO['members']),
        "upload": "Choose Excel File",
        "filters": "Filter Controls",
        "date_range": "Date Range",
        "instructions": "Instructions",
        "kpi_total_sales": "Total Sales",
        "kpi_products_sold": "Products Sold",
        "kpi_sales_after_tax": "Sales After Tax",
        "kpi_rating_avg": "Average Rating",
        "monthly_sales": "Monthly Sales Trend",
        "products_sold": "Products Sold",
        "sales_by_product": "Sales by Product Line",
        "payment_methods": "Payment Methods",
        "rating_by_city": "Rating by City",
        "data_overview": "DATA OVERVIEW",
        "view_raw": "View Raw Data",
        "download_csv": "Download CSV",
        "business_insights": "BUSINESS INSIGHTS",
        "no_data": "Upload Excel file to start analysis",
        "no_sales_col": "No sales-like column detected",
        "no_date_col": "No date-like column detected"
    },
    "Indonesia": {
        "title": "DASHBOARD PENJUALAN SUPERMARKET",
        "subtitle": "Analisis Penjualan, Promo, dan Insight Bisnis",
        "team_info": f"{TEAM_INFO['group_name']}",
        "members": " | ".join(TEAM_INFO['members']),
        "upload": "Pilih File Excel",
        "filters": "Kontrol Filter",
        "date_range": "Rentang Tanggal",
        "instructions": "Instruksi",
        "kpi_total_sales": "Total Penjualan",
        "kpi_products_sold": "Produk Terjual",
        "kpi_sales_after_tax": "Penjualan Setelah Pajak",
        "kpi_rating_avg": "Rata-rata Rating",
        "monthly_sales": "Tren Penjualan Bulanan",
        "products_sold": "Produk Terjual",
        "sales_by_product": "Penjualan per Produk",
        "payment_methods": "Metode Pembayaran",
        "rating_by_city": "Rating per Kota",
        "data_overview": "TINJAUAN DATA",
        "view_raw": "Lihat Data Mentah",
        "download_csv": "Unduh CSV",
        "business_insights": "INSIGHT BISNIS",
        "no_data": "Unggah file Excel untuk memulai analisis",
        "no_sales_col": "Tidak ditemukan kolom penjualan",
        "no_date_col": "Tidak ditemukan kolom tanggal"
    },
    "中文 (Chinese)": {
        "title": "超市销售仪表板",
        "subtitle": "销售绩效、交易分析和业务洞察仪表板",
        "team_info": f"{TEAM_INFO['group_name']}",
        "members": " | ".join(TEAM_INFO['members']),
        "upload": "选择 Excel 文件",
        "filters": "筛选控制",
        "date_range": "日期范围",
        "instructions": "使用说明",
        "kpi_total_sales": "总销售额",
        "kpi_products_sold": "已售产品",
        "kpi_sales_after_tax": "税后销售额",
        "kpi_rating_avg": "平均评分",
        "monthly_sales": "月度销售趋势",
        "products_sold": "已售产品",
        "sales_by_product": "按产品线销售",
        "payment_methods": "支付方式",
        "rating_by_city": "按城市评分",
        "data_overview": "数据概览",
        "view_raw": "查看原始数据",
        "download_csv": "下载 CSV",
        "business_insights": "业务洞察",
        "no_data": "上传 Excel 文件以开始分析",
        "no_sales_col": "未检测到销售列",
        "no_date_col": "未检测到日期列"
    },
    "日本語 (Japanese)": {
        "title": "スーパーマーケット販売ダッシュボード",
        "subtitle": "販売実績、取引分析、ビジネス洞察ダッシュボード",
        "team_info": f"{TEAM_INFO['group_name']}",
        "members": " | ".join(TEAM_INFO['members']),
        "upload": "Excelファイルを選択",
        "filters": "フィルター制御",
        "date_range": "期間",
        "instructions": "説明",
        "kpi_total_sales": "総売上",
        "kpi_products_sold": "販売数量",
        "kpi_sales_after_tax": "税引後売上",
        "kpi_rating_avg": "平均評価",
        "monthly_sales": "月次売上トレンド",
        "products_sold": "販売商品",
        "sales_by_product": "商品別売上",
        "payment_methods": "支払方法",
        "rating_by_city": "都市別評価",
        "data_overview": "データ概要",
        "view_raw": "生データ表示",
        "download_csv": "CSVダウンロード",
        "business_insights": "ビジネス洞察",
        "no_data": "分析を開始するにはExcelファイルをアップロードしてください",
        "no_sales_col": "売上列が検出されません",
        "no_date_col": "日付列が検出されません"
    },
    "한국어 (Korean)": {
        "title": "슈퍼마켓 판매 대시보드",
        "subtitle": "판매 성과, 거래 분석 및 비즈니스 통찰력 대시보드",
        "team_info": f"{TEAM_INFO['group_name']}",
        "members": " | ".join(TEAM_INFO['members']),
        "upload": "엑셀 파일 선택",
        "filters": "필터 제어",
        "date_range": "날짜 범위",
        "instructions": "지침",
        "kpi_total_sales": "총 매출",
        "kpi_products_sold": "판매된 제품",
        "kpi_sales_after_tax": "세후 매출",
        "kpi_rating_avg": "평균 평점",
        "monthly_sales": "월간 판매 추세",
        "products_sold": "판매된 제품",
        "sales_by_product": "제품 라인별 매출",
        "payment_methods": "결제 방법",
        "rating_by_city": "도시별 평점",
        "data_overview": "데이터 개요",
        "view_raw": "원시 데이터 보기",
        "download_csv": "CSV 다운로드",
        "business_insights": "비즈니스 통찰력",
        "no_data": "분석을 시작하려면 Excel 파일을 업로드하세요",
        "no_sales_col": "판매 열이 감지되지 않음",
        "no_date_col": "날짜 열이 감지되지 않음"
    },
    "Italiano (Italian)": {
        "title": "DASHBOARD VENDITE SUPERMERCATO",
        "subtitle": "Dashboard di Performance Vendite, Analisi Affari e Insight Commerciali",
        "team_info": f"{TEAM_INFO['group_name']}",
        "members": " | ".join(TEAM_INFO['members']),
        "upload": "Scegli File Excel",
        "filters": "Controlli Filtri",
        "date_range": "Intervallo Date",
        "instructions": "Istruzioni",
        "kpi_total_sales": "Vendite Totali",
        "kpi_products_sold": "Prodotti Venduti",
        "kpi_sales_after_tax": "Vendite Dopo Tasse",
        "kpi_rating_avg": "Valutazione Media",
        "monthly_sales": "Andamento Vendite Mensili",
        "products_sold": "Prodotti Venduti",
        "sales_by_product": "Vendite per Linea Prodotto",
        "payment_methods": "Metodi di Pagamento",
        "rating_by_city": "Valutazione per Città",
        "data_overview": "PANORAMICA DATI",
        "view_raw": "Visualizza Dati Grezzi",
        "download_csv": "Scarica CSV",
        "business_insights": "INSIGHT COMMERCIALI",
        "no_data": "Carica file Excel per iniziare l'analisi",
        "no_sales_col": "Nessuna colonna vendite rilevata",
        "no_date_col": "Nessuna colonna data rilevata"
    },
    "Deutsch (German)": {
        "title": "SUPERMARKT-VERKAUFS-DASHBOARD",
        "subtitle": "Verkaufsleistung, Deals-Analyse und Geschäftserkenntnisse Dashboard",
        "team_info": f"{TEAM_INFO['group_name']}",
        "members": " | ".join(TEAM_INFO['members']),
        "upload": "Excel-Datei auswählen",
        "filters": "Filtersteuerung",
        "date_range": "Datumsbereich",
        "instructions": "Anweisungen",
        "kpi_total_sales": "Gesamtumsatz",
        "kpi_products_sold": "Verkaufte Produkte",
        "kpi_sales_after_tax": "Umsatz nach Steuern",
        "kpi_rating_avg": "Durchschnittliche Bewertung",
        "monthly_sales": "Monatlicher Umsatzverlauf",
        "products_sold": "Verkaufte Produkte",
        "sales_by_product": "Umsatz nach Produktlinie",
        "payment_methods": "Zahlungsmethoden",
        "rating_by_city": "Bewertung nach Stadt",
        "data_overview": "DATENÜBERBLICK",
        "view_raw": "Rohdaten anzeigen",
        "download_csv": "CSV herunterladen",
        "business_insights": "GESCHÄFTSERKENNTNISSE",
        "no_data": "Laden Sie eine Excel-Datei hoch, um die Analyse zu starten",
        "no_sales_col": "Keine Verkaufs-Spalte gefunden",
        "no_date_col": "Keine Datums-Spalte gefunden"
    },
    "Français (French)": {
        "title": "TABLEAU DE BORD DES VENTES SUPERMARCHÉ",
        "subtitle": "Dashboard de Performance des Ventes, Analyse des Transactions et Insights Business",
        "team_info": f"{TEAM_INFO['group_name']}",
        "members": " | ".join(TEAM_INFO['members']),
        "upload": "Choisir un fichier Excel",
        "filters": "Contrôles de Filtre",
        "date_range": "Plage de Dates",
        "instructions": "Instructions",
        "kpi_total_sales": "Ventes Totales",
        "kpi_products_sold": "Produits Vendus",
        "kpi_sales_after_tax": "Ventes Après Taxes",
        "kpi_rating_avg": "Note Moyenne",
        "monthly_sales": "Tendance des Ventes Mensuelles",
        "products_sold": "Produits Vendus",
        "sales_by_product": "Ventes par Ligne de Produit",
        "payment_methods": "Modes de Paiement",
        "rating_by_city": "Note par Ville",
        "data_overview": "APERÇU DES DONNÉES",
        "view_raw": "Afficher les Données Brutes",
        "download_csv": "Télécharger CSV",
        "business_insights": "INSIGHTS BUSINESS",
        "no_data": "Téléversez un fichier Excel pour démarrer l'analyse",
        "no_sales_col": "Aucune colonne de ventes détectée",
        "no_date_col": "Aucune colonne de date détectée"
    },
    "Nederlands (Dutch)": {
        "title": "SUPERMARKT VERKOOP DASHBOARD",
        "subtitle": "Dashboard voor Verkoopprestaties, Dealanalyse en Bedrijfsinzichten",
        "team_info": f"{TEAM_INFO['group_name']}",
        "members": " | ".join(TEAM_INFO['members']),
        "upload": "Kies Excel-bestand",
        "filters": "Filterbesturing",
        "date_range": "Datumbereik",
        "instructions": "Instructies",
        "kpi_total_sales": "Totale Verkoop",
        "kpi_products_sold": "Verkochte Producten",
        "kpi_sales_after_tax": "Verkoop na Belasting",
        "kpi_rating_avg": "Gemiddelde Beoordeling",
        "monthly_sales": "Maandelijkse Verkooptrend",
        "products_sold": "Verkochte Producten",
        "sales_by_product": "Verkoop per Productlijn",
        "payment_methods": "Betalingsmethoden",
        "rating_by_city": "Beoordeling per Stad",
        "data_overview": "DATA OVERZICHT",
        "view_raw": "Ruwe Gegevens Bekijken",
        "download_csv": "CSV Downloaden",
        "business_insights": "BEDRIJFSINZICHTEN",
        "no_data": "Upload een Excel-bestand om de analyse te starten",
        "no_sales_col": "Geen verkoopkolom gedetecteerd",
        "no_date_col": "Geen datumkolom gedetecteerd"
    },
    "العربية (Arabic)": {
        "title": "لوحة تحكم مبيعات السوبرماركت",
        "subtitle": "لوحة تحكم أداء المبيعات وتحليل الصفقات ورؤى الأعمال",
        "team_info": f"{TEAM_INFO['group_name']}",
        "members": " | ".join(TEAM_INFO['members']),
        "upload": "اختر ملف Excel",
        "filters": "ضوابط التصفية",
        "date_range": "نطاق التاريخ",
        "instructions": "التعليمات",
        "kpi_total_sales": "إجمالي المبيعات",
        "kpi_products_sold": "المنتجات المباعة",
        "kpi_sales_after_tax": "المبيعات بعد الضريبة",
        "kpi_rating_avg": "متوسط التقييم",
        "monthly_sales": "اتجاه المبيعات الشهرية",
        "products_sold": "المنتجات المباعة",
        "sales_by_product": "المبيعات حسب خط الإنتاج",
        "payment_methods": "طرق الدفع",
        "rating_by_city": "التقييم حسب المدينة",
        "data_overview": "نظرة عامة على البيانات",
        "view_raw": "عرض البيانات الخام",
        "download_csv": "تنزيل CSV",
        "business_insights": "رؤى الأعمال",
        "no_data": "قم بتحميل ملف Excel لبدء التحليل",
        "no_sales_col": "لم يتم اكتشاف عمود المبيعات",
        "no_date_col": "لم يتم اكتشاف عمود التاريخ"
    },
    "Español (Spanish)": {
        "title": "TABLERO DE VENTAS SUPERMERCADO",
        "subtitle": "Tablero de Rendimiento de Ventas, Análisis de Transacciones e Información Comercial",
        "team_info": f"{TEAM_INFO['group_name']}",
        "members": " | ".join(TEAM_INFO['members']),
        "upload": "Elegir Archivo Excel",
        "filters": "Controles de Filtro",
        "date_range": "Rango de Fechas",
        "instructions": "Instrucciones",
        "kpi_total_sales": "Ventas Totales",
        "kpi_products_sold": "Productos Vendidos",
        "kpi_sales_after_tax": "Ventas Después de Impuestos",
        "kpi_rating_avg": "Calificación Promedio",
        "monthly_sales": "Tendencia de Ventas Mensuales",
        "products_sold": "Productos Vendidos",
        "sales_by_product": "Ventas por Línea de Producto",
        "payment_methods": "Métodos de Pago",
        "rating_by_city": "Calificación por Ciudad",
        "data_overview": "VISIÓN DE DATOS",
        "view_raw": "Ver Datos Crudos",
        "download_csv": "Descargar CSV",
        "business_insights": "INFORMACIÓN COMERCIAL",
        "no_data": "Suba un archivo Excel para comenzar el análisis",
        "no_sales_col": "No se detectó columna de ventas",
        "no_date_col": "No se detectó columna de fecha"
    },
    "Português (Portuguese)": {
        "title": "PAINEL DE VENDAS SUPERMERCADO",
        "subtitle": "Painel de Desempenho de Vendas, Análise de Transações e Insights de Negócios",
        "team_info": f"{TEAM_INFO['group_name']}",
        "members": " | ".join(TEAM_INFO['members']),
        "upload": "Escolher Arquivo Excel",
        "filters": "Controles de Filtro",
        "date_range": "Intervalo de Datas",
        "instructions": "Instruções",
        "kpi_total_sales": "Vendas Totais",
        "kpi_products_sold": "Produtos Vendidos",
        "kpi_sales_after_tax": "Vendas Após Impostos",
        "kpi_rating_avg": "Avaliação Média",
        "monthly_sales": "Tendência de Vendas Mensais",
        "products_sold": "Produtos Vendidos",
        "sales_by_product": "Vendas por Linha de Produto",
        "payment_methods": "Métodos de Pagamento",
        "rating_by_city": "Avaliação por Cidade",
        "data_overview": "VISÃO GERAL DOS DADOS",
        "view_raw": "Ver Dados Brutos",
        "download_csv": "Baixar CSV",
        "business_insights": "INSIGHTS DE NEGÓCIOS",
        "no_data": "Carregue um arquivo Excel para iniciar a análise",
        "no_sales_col": "Nenhuma coluna de vendas detectada",
        "no_date_col": "Nenhuma coluna de data detectada"
    }
}

# ===================== CUSTOM CSS =====================
st.markdown(
    f"""
    <style>
        .team-header {{
            background: linear-gradient(135deg, {PRIMARY_START} 0%, {PRIMARY_END} 100%);
            padding: 1.2rem;
            border-radius: 10px;
            color: white;
            margin-bottom: 1.5rem;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }}
        .team-name {{
            font-weight: 800;
            font-size: 1.4rem;
            margin-bottom: 0.5rem;
            text-align: center;
        }}
        .team-members {{
            font-size: 1rem;
            line-height: 1.4;
            text-align: center;
            opacity: 0.9;
        }}
        .main-header {{
            background: linear-gradient(135deg, {PRIMARY_START} 0%, {PRIMARY_END} 100%);
            padding: 1.3rem;
            border-radius: 10px;
            color: white;
            text-align: center;
            margin-bottom: 1.5rem;
            box-shadow: 0 6px 12px rgba(0,0,0,0.12);
        }}
        .kpi-box {{
            background: white;
            padding: 1rem;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.08);
            border-left: 6px solid {PRIMARY_START};
            margin-bottom: 0.8rem;
            text-align: center;
        }}
        .kpi-label {{
            font-size: 0.9rem;
            color: #666;
            margin-bottom: 0.5rem;
            font-weight: 600;
        }}
        .kpi-value {{
            font-size: 1.5rem;
            font-weight: 800;
            color: {PRIMARY_START};
            margin-bottom: 0.2rem;
        }}
        .sidebar-header {{
            font-size: 1.05rem;
            font-weight: 600;
            color: {PRIMARY_START};
            margin-top: 0.6rem;
        }}
        .chart-title {{
            font-size: 1.1rem;
            font-weight: 700;
            margin-bottom: .8rem;
            padding-bottom: .4rem;
            border-bottom: 2px solid {PRIMARY_START};
            color: {PRIMARY_START};
        }}
        .stDownloadButton > button {{
            background-color: {PRIMARY_START};
            color: white;
            font-weight: 600;
        }}
        .stButton > button:hover {{
            background-color: {PRIMARY_END};
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# ===================== SIDEBAR =====================
with st.sidebar:
    # Language selection
    lang_options = list(TRANSLATIONS.keys())
    lang = st.selectbox(
        "🌐 Select Language / Pilih Bahasa",
        lang_options,
        index=1  # Default to Indonesia
    )
    tr = TRANSLATIONS.get(lang, TRANSLATIONS["English"])
    
    # File upload
    st.markdown(f"## 📁 {tr['upload']}")
    uploaded_file = st.file_uploader(tr["upload"], type=["xlsx", "xls"], label_visibility="collapsed")
    
    st.markdown("---")
    
    # Filters
    st.markdown(f'<div class="sidebar-header">🔍 {tr["filters"]}</div>', unsafe_allow_html=True)
    
    filter_widgets = {}
    
    if uploaded_file:
        try:
            df = pd.read_excel(uploaded_file)
            
            # Create filters for categorical columns
            categorical_cols = ['Branch', 'City', 'Customer type', 'Gender', 'Product line', 'Payment']
            
            for col in categorical_cols:
                if col in df.columns:
                    unique_vals = df[col].dropna().unique().tolist()
                    if len(unique_vals) > 0:
                        selected = st.multiselect(f"{col} Filter", options=unique_vals, default=unique_vals)
                        filter_widgets[col] = selected
            
            # Date filter
            if 'Date' in df.columns:
                df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
                min_date = df['Date'].min().date()
                max_date = df['Date'].max().date()
                date_range = st.date_input(
                    tr["date_range"],
                    (min_date, max_date),
                    min_value=min_date,
                    max_value=max_date
                )
                if len(date_range) == 2:
                    filter_widgets['Date'] = date_range
                    
        except Exception as e:
            st.error(f"Error reading file: {e}")
    
    st.markdown("---")
    st.markdown(f"### ℹ {tr['instructions']}")
    st.write(
        "1. Upload Excel file  \n"
        "2. Apply filters as needed  \n"
        "3. View KPIs and visualizations  \n"
        "4. Download processed data"
    )

# ===================== TEAM INFO IN MAIN HEADER =====================
st.markdown(
    f'''
    <div class="team-header">
        <div class="team-name">📚 {TEAM_INFO['group_name']}</div>
        <div class="team-members">
            {' | '.join(TEAM_INFO['members'])}
        </div>
    </div>
    ''',
    unsafe_allow_html=True
)

# ===================== MAIN HEADER =====================
st.markdown(f'<div class="main-header"><h1 style="margin:0;">🛒 {tr["title"]}</h1><p style="margin:0; opacity:0.95;">{tr["subtitle"]}</p></div>', unsafe_allow_html=True)

if not uploaded_file:
    st.info(tr["no_data"])
    st.stop()

# ===================== DATA LOADING =====================
@st.cache_data
def load_data(file):
    return pd.read_excel(file)

df = load_data(uploaded_file)

# ===================== APPLY FILTERS =====================
df_filtered = df.copy()

for col, val in filter_widgets.items():
    if col not in df_filtered.columns:
        continue
    if isinstance(val, list):
        if val:
            df_filtered = df_filtered[df_filtered[col].isin(val)]
    elif isinstance(val, tuple) and len(val) == 2 and col == 'Date':
        start_date, end_date = pd.to_datetime(val[0]), pd.to_datetime(val[1])
        if 'Date' in df_filtered.columns:
            df_filtered['Date'] = pd.to_datetime(df_filtered['Date'], errors='coerce')
            df_filtered = df_filtered[(df_filtered['Date'] >= start_date) & (df_filtered['Date'] <= end_date)]

# ===================== KPI CALCULATIONS =====================
total_sales = df_filtered['Total'].sum() if 'Total' in df_filtered.columns else 0
total_quantity = df_filtered['Quantity'].sum() if 'Quantity' in df_filtered.columns else 0
average_rating = df_filtered['Rating'].mean() if 'Rating' in df_filtered.columns else 0

# Sales after tax = Total - Tax
if 'Total' in df_filtered.columns and 'Tax 5%' in df_filtered.columns:
    total_tax = df_filtered['Tax 5%'].sum()
    sales_after_tax = total_sales - total_tax
else:
    sales_after_tax = None

# ===================== KPI DISPLAY IN BOXES =====================
st.markdown("## 📊 " + tr["data_overview"])

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(
        f"""
        <div class="kpi-box">
            <div class="kpi-label">{tr["kpi_total_sales"]}</div>
            <div class="kpi-value">${total_sales:,.2f}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div class="kpi-box">
            <div class="kpi-label">{tr["kpi_products_sold"]}</div>
            <div class="kpi-value">{total_quantity:,.0f}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    sales_after_tax_display = f"${sales_after_tax:,.2f}" if sales_after_tax is not None else "N/A"
    st.markdown(
        f"""
        <div class="kpi-box">
            <div class="kpi-label">{tr["kpi_sales_after_tax"]}</div>
            <div class="kpi-value">{sales_after_tax_display}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col4:
    rating_display = f"{average_rating:.1f}" if 'Rating' in df_filtered.columns else "N/A"
    st.markdown(
        f"""
        <div class="kpi-box">
            <div class="kpi-label">{tr["kpi_rating_avg"]}</div>
            <div class="kpi-value">{rating_display}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ===================== CHART 1 — MONTHLY SALES =====================
st.markdown(f'<div class="chart-title">📅 {tr["monthly_sales"]}</div>', unsafe_allow_html=True)

if 'Date' in df_filtered.columns and 'Total' in df_filtered.columns:
    df_temp = df_filtered.copy()
    df_temp['Date'] = pd.to_datetime(df_temp['Date'], errors='coerce')
    df_temp = df_temp.dropna(subset=['Date', 'Total'])
    
    if not df_temp.empty:
        # Extract month-year
        df_temp['Month_Year'] = df_temp['Date'].dt.to_period('M').astype(str)
        
        # Group by month
        monthly_sales = df_temp.groupby('Month_Year')['Total'].sum().reset_index()
        monthly_sales = monthly_sales.sort_values('Month_Year')
        
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(
            x=monthly_sales['Month_Year'],
            y=monthly_sales['Total'],
            mode='lines+markers',
            line=dict(color=LINE_COLOR, width=3),
            marker=dict(size=6),
            fill='tozeroy',
            fillcolor='rgba(255, 0, 51, 0.1)',
            name='Total Sales'
        ))
        
        fig1.update_layout(
            xaxis_title='Month',
            yaxis_title='Total Sales ($)',
            template='plotly_white',
            hovermode='x unified',
            margin=dict(t=30, b=20, l=40, r=20),
            plot_bgcolor='rgba(240, 240, 240, 0.1)'
        )
        
        st.plotly_chart(fig1, use_container_width=True)
    else:
        st.warning("No date data available for chart")
else:
    st.warning("Date or Total columns not found for monthly sales chart")

# ===================== PRODUCT CHARTS =====================
colA, colB = st.columns(2)

with colA:
    st.markdown(f'<div class="chart-title">📦 {tr["products_sold"]}</div>', unsafe_allow_html=True)
    
    if 'Product line' in df_filtered.columns and 'Quantity' in df_filtered.columns:
        product_qty = df_filtered.groupby('Product line')['Quantity'].sum().reset_index()
        product_qty = product_qty.sort_values('Quantity', ascending=False)
        
        fig2 = px.bar(
            product_qty.head(10),
            x='Product line',
            y='Quantity',
            labels={'Product line': 'Product Category', 'Quantity': 'Units Sold'},
            color='Quantity',
            color_continuous_scale=['lightblue', PRIMARY_START]
        )
        
        fig2.update_layout(
            template='plotly_white',
            showlegend=False,
            xaxis_tickangle=-45,
            plot_bgcolor='rgba(240, 240, 240, 0.1)'
        )
        
        st.plotly_chart(fig2, use_container_width=True)
    else:
        st.warning("Product line or Quantity data not available")

with colB:
    st.markdown(f'<div class="chart-title">📊 {tr["sales_by_product"]}</div>', unsafe_allow_html=True)
    
    if 'Product line' in df_filtered.columns and 'Total' in df_filtered.columns:
        product_sales = df_filtered.groupby('Product line')['Total'].sum().reset_index()
        product_sales = product_sales.sort_values('Total', ascending=False)
        
        fig3 = px.bar(
            product_sales.head(10),
            x='Product line',
            y='Total',
            labels={'Product line': 'Product Category', 'Total': 'Total Sales ($)'},
            color='Total',
            color_continuous_scale=['lightcoral', LINE_COLOR]
        )
        
        fig3.update_layout(
            template='plotly_white',
            showlegend=False,
            xaxis_tickangle=-45,
            plot_bgcolor='rgba(240, 240, 240, 0.1)'
        )
        
        st.plotly_chart(fig3, use_container_width=True)
    else:
        st.warning("Product line or Total data not available")

# ===================== PAYMENT AND RATING CHARTS =====================
colC, colD = st.columns(2)

with colC:
    st.markdown(f'<div class="chart-title">💳 {tr["payment_methods"]}</div>', unsafe_allow_html=True)
    
    if 'Payment' in df_filtered.columns:
        payment_counts = df_filtered['Payment'].value_counts().reset_index()
        payment_counts.columns = ['Payment Method', 'Count']
        
        fig4 = px.pie(
            payment_counts,
            names='Payment Method',
            values='Count',
            hole=0.4,
            color_discrete_sequence=px.colors.sequential.RdBu
        )
        
        fig4.update_traces(
            textposition='inside',
            textinfo='percent+label',
            pull=[0.05] * len(payment_counts)
        )
        
        st.plotly_chart(fig4, use_container_width=True)
    else:
        st.warning("Payment method data not available")

with colD:
    st.markdown(f'<div class="chart-title">⭐ {tr["rating_by_city"]}</div>', unsafe_allow_html=True)
    
    if 'City' in df_filtered.columns and 'Rating' in df_filtered.columns:
        city_rating = df_filtered.groupby('City')['Rating'].mean().reset_index()
        city_rating = city_rating.sort_values('Rating', ascending=False)
        
        fig5 = px.bar(
            city_rating,
            x='City',
            y='Rating',
            labels={'City': 'City', 'Rating': 'Average Rating'},
            color='Rating',
            color_continuous_scale=['yellow', 'green']
        )
        
        fig5.update_layout(
            template='plotly_white',
            showlegend=False,
            yaxis_range=[0, 10],
            plot_bgcolor='rgba(240, 240, 240, 0.1)'
        )
        
        st.plotly_chart(fig5, use_container_width=True)
    else:
        st.warning("City or Rating data not available")

# ===================== DATA TABLE + DOWNLOAD =====================
st.markdown("---")
st.markdown(f"## 📋 {tr['data_overview']}")

with st.expander(tr["view_raw"], expanded=False):
    st.dataframe(df_filtered, use_container_width=True)
    
    # Add download button
    csv = df_filtered.to_csv(index=False).encode('utf-8')
    st.download_button(
        label=tr["download_csv"],
        data=csv,
        file_name="supermarket_sales_filtered.csv",
        mime="text/csv"
    )

# ===================== BUSINESS INSIGHTS =====================
st.markdown("---")
st.markdown(f"## 💡 {tr['business_insights']}")

insight_col1, insight_col2, insight_col3 = st.columns(3)

# Insight 1: Top performing product
if 'Product line' in df_filtered.columns and 'Total' in df_filtered.columns:
    top_product = df_filtered.groupby('Product line')['Total'].sum().idxmax()
    top_product_sales = df_filtered.groupby('Product line')['Total'].sum().max()
    
    with insight_col1:
        st.info(f"Top Product Category: {top_product}  \n"
                f"Sales: ${top_product_sales:,.2f}")

# Insight 2: Best performing city
if 'City' in df_filtered.columns and 'Total' in df_filtered.columns:
    top_city = df_filtered.groupby('City')['Total'].sum().idxmax()
    top_city_sales = df_filtered.groupby('City')['Total'].sum().max()
    
    with insight_col2:
        st.success(f"Best Performing City: {top_city}  \n"
                  f"Sales: ${top_city_sales:,.2f}")

# Insight 3: Customer type analysis
if 'Customer type' in df_filtered.columns and 'Total' in df_filtered.columns:
    customer_avg = df_filtered.groupby('Customer type')['Total'].mean()
    best_customer_type = customer_avg.idxmax()
    avg_sale = customer_avg.max()
    
    with insight_col3:
        st.warning(f"Highest Average Sale: {best_customer_type} customers  \n"
                  f"Average: ${avg_sale:,.2f}")

# ===================== FOOTER =====================
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666; font-size: 0.9rem; padding: 1rem;'>
        Dashboard created with by Group 7 - Business Mathematics | 
        Using Streamlit, Plotly, and Pandas | 
        Supermarket Sales Analysis Dashboard
    </div>
    """,
    unsafe_allow_html=True
)