import sys
import os
import os.path as osp
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plot OTTR RDF instances.')
    parser.add_argument('-format', '--format', default='png',
                        help='output file format, e.g. png, pdf')
    parser.add_argument('in_dir', default='./data', help='directory holding the OTTR instances')
    parser.add_argument('lib_file', default='./data/template_library.stottr', help='directory holding the OTTR library')
    parser.add_argument('-rdf_dir', '--rdf_dir', help='if specified: directory for storing the RDF instances')
    parser.add_argument('-viz_dir', '--viz_dir', help='if specified: directory for outputting the visualizations')
    args = parser.parse_args()

    ottr_instances_path=rdf_output_path=viz_output_path = args.in_dir
    if args.rdf_dir is not None:
        rdf_output_path = args.rdf_dir
    if args.viz_dir is not None:
        viz_output_path = args.viz_dir

    stottr_files = list(filter(lambda filename: filename.endswith('.stottr'), os.listdir(ottr_instances_path)))
    if args.lib_file in stottr_files:
        stottr_files.remove(args.lib_file)
    if len(stottr_files) == 0:
        print('No stottr instances found.')
        sys.exit()

    # find all .stottr files in the input directory and create a viz for each
    for stottr_file in stottr_files:
        file_name = stottr_file[:-7]
        print(f'Viz OTTR template: {file_name}')

        # ottr to ttl
        os.system(
            f'java -jar ~/Lutra/lutra/lutra-cli/target/lutra.jar --library {args.lib_file} --libraryFormat stottr --inputFormat stottr --output {osp.join(rdf_output_path, file_name)} {osp.join(ottr_instances_path, stottr_file)} > /dev/null')

        # ttl to dot
        os.system(
            f'rapper -i turtle -o dot {osp.join(rdf_output_path, file_name + ".ttl")} > {osp.join(viz_output_path, file_name + ".dot")}')

        # vis dot
        os.system(
            f'dot -T{args.format} -o{osp.join(viz_output_path, file_name + "." + args.format)} {osp.join(viz_output_path, file_name + ".dot")}')

    print('done.')
